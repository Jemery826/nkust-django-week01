
from django.contrib import admin
from django.urls import path
from mysite import views #匯入views.index

urlpatterns = [
    path('admin/', admin.site.urls),  #後台程式
    path('date/', views.date),  #產生/date的頁面
    path('lotto/', views.lotto),
    path('dashboard/', views.dashboard),
    path('play/<int:id>/', views.play), #id為int數值
    path('',views.index),  #首頁為views.index的程式
]
