"""
URL configuration for _bitbank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ViewHome.as_view(), name="home"),
    path('about/', ViewAbout.as_view(), name="about"),
    path('legal/', ViewLegal.as_view(), name="legal"),
    path('test/', ViewQuerys, name="query"),
    path('accounts/', include('allauth.urls')),
    path('account/', include('appAccounts.urls')),
    path('logs/', include('appLogs.urls')),
    path('transactions/', include('appTransactions.urls')),
    path('wallet/', include('appWallets.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)