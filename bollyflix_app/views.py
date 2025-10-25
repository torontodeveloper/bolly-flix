from django.shortcuts import render
from bollyflix_app.models import Movie
from django.http import HttpResponse,JsonResponse

# Create your views here.

def movie_list(request):
    query_set = Movie.objects.all()
    print(f'query set is {query_set}')
    print(f'query set is {type(query_set)}')
    return JsonResponse(list(query_set.values()),safe=False)

def get_movie(request,id):
    print('id',id,type(id))
    movie = Movie.objects.get(pk=id)
    print('movie',movie,movie.description,movie.active)
    result = {
        "name" : movie.name,
        "description":movie.description,
        "active":movie.active
    }
    return JsonResponse(result,safe=False)