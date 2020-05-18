"""Travelwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('destinations/admin/', admin.site.urls),
    path('about/admin/', admin.site.urls),
    path('destinations/about/admin/', admin.site.urls),
    path('', include('landingpage.urls')),
    path('signup/',include('signup.urls')),
    path('signin/', include('signin.urls')),
    path('logout/', include("logout.urls")),
    path('about/logout/', include("logout.urls")),
    path('about/', include("about.urls")),
    path('destinations/about/', include("about.urls")),
    path('sms/', include("sms_sending.urls")),
    path('subscribe/', include('subscribe.urls')),
    path('destinations/', include('destinations.urls')),
    path('destinations/subscribe/', include('subscribe.urls')),
    path('signin/signup/', include('signup.urls')),
    path('signup/signin/', include('signin.urls')),
    path('signin/signup/signin/', include('signin.urls')),
    path('destinations/signup/', include('signup.urls')),
    path('destinations/signin/', include('signin.urls')),
    path('destinations/logout/', include("logout.urls")),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
