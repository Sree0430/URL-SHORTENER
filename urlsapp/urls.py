from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten', views.shorten, name='shorten'),
    path('<str:code>', views.follow, name='follow'),
]
