from django.http import Http404
from .models import Movie
from django.shortcuts import render
# Create your views here.
def  index(request):
	all_movies=Movie.objects.all()
	context = {
		'all_movies': all_movies,
	}
	return render(request, 'movie1/index.html',context)
def  detail(request, movie_id):
	try:
		m1=Movie.objects.get(pk=movie_id)
	except Movie.DoesNotExist:
		raise Http404("this is wrong movie id")
	return render(request, 'movie1/index1.html', {'m1':m1})