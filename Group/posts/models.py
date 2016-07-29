from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model): #creates a class which creates objects
	title = models.CharField(max_length=100)
	content = models.TextField()
	update = models.DateTimeField(auto_now=True, auto_now_add=False)			#when last saved
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True) #when added initially

	def __str__(self):
		return self.title #this whole function is used to create human readable string
	def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'id':self.id})

# Create your models here.
