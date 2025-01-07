from django.urls import path
from .views import *

urlpatterns = [
    path('completation/', ViewCompletation.as_view(), name="completation"),
    path('validate-username/', ViewRedirect, name='validate_username'),
    path('profile/', ViewAccount.as_view(), name="account"),
    path('login/', ViewLogin.as_view(), name='login'),
    path('signup/', ViewSignup.as_view(), name='signup')
]