from openai import OpenAI
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

client = OpenAI(api_key='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')

# Create your views here.
def generate_response(question):
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield(chunk.choices[0].delta.content)

@csrf_exempt
def answer(request):
    data = json.loads(request.body)
    message = data["message"]
    #message = "Describe django in 100 words."
    response = StreamingHttpResponse(generate_response(message), status=200, content_type="text/plain") 
    return response

def chatbot_page(request, user):
    return render(request, 'chatbot/chatbot.html')