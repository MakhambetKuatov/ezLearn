from django.urls import path
from . import views

urlpatterns = [
    path('home', views.base),
    path('home/lessons', views.lessons),
    path('home/product', views.product),
    path('home/profile', views.profile)
]