from openai import OpenAI
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

client = OpenAI(api_key=#Api de Open AI)

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
    response = StreamingHttpResponse(generate_response(message), status=200, content_type="text/plain") 
    return response

def chatbot_page(request, user):
    return render(request, 'chatbot/chatbot.html')