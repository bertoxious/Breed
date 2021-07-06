from django.db import models
from homepage.models import Dog
from datetime import datetime 
dt = datetime.now()
# Create your models here.

class Dogcomment(models.Model):
	dog = models.ForeignKey(Dog, related_name='dog_comments',on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	comment = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{} commented on {}'.format(self.name, self.date_added)