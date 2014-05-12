from django.test import TestCase

# Create your tests here.
from .models import Artist

class TestArtists(TestCase):

	def setUp(self):
		self.artist = Artist.objects.create(first_name = 'David', last_name = 'Bow')

	def test_existe_vista(self):
		res=  self.client.get('/artists/%d/' % self.artist.id)
		self.assertEqual(res.status_code,200)
		self.assertTrue('david' in res.content)