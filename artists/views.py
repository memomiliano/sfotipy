from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Artist

class ArtistDetailsView(DetailView):
    model = Artist
    context_object_name = 'artist'
    
    def get_template_names(self):
        return 'artista.html'