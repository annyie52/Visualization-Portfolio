from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('purpose/', views.purpose),
    path('review/', views.review)
]