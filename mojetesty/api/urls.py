from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutest),
    path('test/<str:pk>/', views.getTest),
    path('test/<str:pk>/add/', views.addTest),
]