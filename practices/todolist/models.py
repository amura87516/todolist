from django.db import models

# Create your models here.

from django.utils import timezone
import datetime

class tobedone(models.Model):
    
	def __str__(self):              
		return self.title
	def exp(self):
		return self.deadline >= timezone.now()

	user=models.CharField(max_length=200)
	title= models.CharField(max_length=200)
	detail= models.TextField(blank=True)
	deadline = models.DateField()
	pub_date = models.DateTimeField('date published')
	finish= models.BooleanField(default=False)
        
