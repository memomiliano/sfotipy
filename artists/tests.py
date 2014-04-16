from django.test import TestCase
from .models as Artist

class TestArtists(TestCase):
    
    def setUp(self):
        self.artist = Artist.objects.create(first_name='david', last_name='bowie')
        
    def text_existe-vista(self):
        print(self.client.get('/artists/%d/' % self.artist.id))