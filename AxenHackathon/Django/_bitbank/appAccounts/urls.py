from django.urls import path
from .views import *

urlpatterns = [
    path('completation/', ViewCompletation.as_view(), name="completation"),
    path('validate-username/', ViewRedirect, name='validate_username'),
    path('profile/', ViewAccount.as_view(), name="account"),
    path('login/', ViewLoginUser, name='login'),
    path('signup/', ViewRegisterUser, name='signup'),
    path('register/', ViewRegisterUser, name="register"),
]