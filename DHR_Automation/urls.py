"""
URL configuration for DHR_Automation project.

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
from django.urls import path
from login_page.views import login
from sign_up_page.views import signup
from home_page.views import button_action
from SMT_DHR_page.views import SMT
# from SMT_DHR_page.views import username

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('signup/',signup),
    path('home/',button_action),
    path('SMT-DHR/',SMT),
]
