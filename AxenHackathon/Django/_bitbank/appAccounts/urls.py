from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('completation/', ViewCompletation.as_view(), name="completation"),
    path('validate-username/', ViewRedirect, name='validate_username'),
    path('profile/', ViewAccount, name="account"),
    path('login/', ViewLoginUser, name='login'),
    path('signup/', ViewRegisterUser, name='signup'),
    path('register/', ViewRegisterUser, name="register"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='recovery/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='recovery/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='recovery/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='recovery/password_reset_complete.html'), name='password_reset_complete'), 
]