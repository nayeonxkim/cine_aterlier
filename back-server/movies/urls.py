from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('<int:movie_pk>/', views.detail),
    path('<int:movie_pk>/rating/', views.rating),
    
]
