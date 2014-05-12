from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Artist(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255, blank = True)
	biography  = models.TextField(blank = True)
	fav_songs = models.ManyToManyField('tracks.Track', blank=True, related_name = 'fav_artist')
	slug = models.SlugField(('slug'), max_length=60, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.first_name) #Or whatever you want the slug to use
       		super(Artist, self).save(*args, **kwargs)

	def es_pharrel(self):
		return self.id == 1

	@staticmethod
	def autocomplete_search_fields():
		return ("id_iexact", "first_name__icontains","last_name__icontains")

	def __unicode__(self):
		return self.first_name