from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('stones/', views.stones, name='stones'),
    path('stones/<pk>', views.stone_detail, name='stone_detail')
]
