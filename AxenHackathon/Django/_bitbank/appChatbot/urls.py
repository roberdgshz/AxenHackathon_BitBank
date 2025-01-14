from django.urls import path
from .views import *

urlpatterns = [
    path('<str:user>', chatbot_page, name='chatbot_page'),
    path('answer/', answer, name='answer'),
]