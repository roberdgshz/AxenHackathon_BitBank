from django.urls import path
from .views import *

app_name = 'contacts'

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('add/', add_contact, name='add_contact'),
    path('remove/<int:contact_id>/', remove_contact, name='remove_contact'),
]