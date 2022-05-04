from django.urls import path
from . import views

urlpatterns=[
    path('', views.mainpage),
    path('hypothesis1/', views.hy1),
    path('hypothesis2/', views.hy2),
    path('hypothesis3/', views.hy3),
    path('hypothesis4/', views.hy4),
    path('hypothesis5/', views.hy5),
    path('insight/', views.insight)
]