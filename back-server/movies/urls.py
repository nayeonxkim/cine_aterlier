from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('index/<int:genreId>/', views.genre),
    path('<int:movie_pk>/', views.detail),
    path('<int:movie_pk>/rating/', views.rating),
    path('<int:movie_pk>/img/', views.img),
    path('karlo/<int:movieId1>/<int:movieId2>/<str:painter>/', views.getKarloImg)
    
]
