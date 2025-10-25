from django.contrib import admin
from django.urls import path
from .views import movie_list,get_movie

urlpatterns = [
    path('list/', movie_list,name='movies-list'),
    path('list/<int:id>/', get_movie,name='movie-detail'),
]
