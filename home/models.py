from django.db import models

class Catogiries(models.Model):
	catogiry =  models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return (" Catogiry: "+self.catogiry)	
 
