from django.db import models

# Create your models here.

class profile(models.Model):
	name = models.CharField(max_length=1200)
	description = models.TextField(default='Description default')
	location= models.CharField(max_length=1200, default='My location', blank= True)
	job = models.CharField(max_length=1200, null = True, blank= True)
	






	def __unicode__(self):
		return self.name



