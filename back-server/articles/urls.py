from django.urls import path
from . import views

# app_name = 'articles'

urlpatterns = [
    path('index/', views.index),
    path('create/', views.create),
    # path('<int:article_pk>/', views.detail),
    # path('update/<int:article_pk>/', views.update)
]
