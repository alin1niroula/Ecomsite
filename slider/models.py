from django.db import models

# Create your models here.

class Slider(models.Model):
	name = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	description = models.TextField(blank = True)
	url = models.URLField(max_length = 500)
	def __str__(self):
		return self.name