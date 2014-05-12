from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Artist

class ArtistDetailView(DetailView):
	model = Artist
	context_object_name = 'fav_artist'
	template_name = 'artists.html'

class ArtistListView(DetailView):
	model = Artist
	context_object_name = 'fav_artist'
	template_name = 'artists.html'
	
	def blog_view(request, slug):
	    blog = Blog.objects.get(slug=slug)
	    #Then do whatever you want


from rest_framework import viewsets
from .serializers import ArtistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
	model = Artist
	serializer_class = ArtistSerializer
	paginate_by =1 
	filter_fields= ('id',)


