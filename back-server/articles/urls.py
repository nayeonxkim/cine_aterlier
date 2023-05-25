from django.urls import path
from . import views

# app_name = 'articles'

urlpatterns = [
    path('index/', views.index),
    path('create/', views.create),
    path('<int:article_pk>/', views.detail),
    path('update/<int:article_pk>/', views.update),
    path('delete/<int:article_pk>/', views.delete),
    path('<int:article_pk>/comment_create/', views.comment_create),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete),
    path('<int:article_pk>/likes/', views.likes),
]
