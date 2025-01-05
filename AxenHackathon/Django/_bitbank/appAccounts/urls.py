from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewCompletation.as_view(), name="completation"),
    path('base/', ViewBase.as_view(), name="base"),
    path('validate-username/', ViewValidateUsername, name='validate_username'),
]