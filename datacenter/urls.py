"""datacenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from mysite import views #匯入views.index

urlpatterns = [
    path('admin/', admin.site.urls),  #後台程式
    path('date/', views.date),  #產生/date的頁面
    path('lotto/', views.lotto),
    path('dashboard/', views.dashboard),
    path('',views.index),  #首頁為views.index的程式
]
