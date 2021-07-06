from django.db import models

# Create your models here.

class Cattle(models.Model):
	breed_name = models.CharField(max_length=200)
	country_origin = models.CharField(max_length=200)
	conservation_status = models.CharField(max_length=200)
	distribution = models.CharField(max_length=500)
	used_for = models.CharField(max_length=200)
	weight = models.CharField(max_length=200)
	skin_color = models.CharField(max_length= 200)
	coat = models.CharField(max_length=200)
	horn_status = models.CharField(max_length=200)
	characteristics = models.CharField(max_length=10000)
	history = models.CharField(max_length=10000)
	breed_image = models.ImageField()

	def __str__(self):
		return self.breed_name
		
class CommentonCattle(models.Model):
    cattle = models.ForeignKey(Cattle,related_name='cattle_comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} commented on {} - at {}'.format(self.name,self.cattle,self.date_added)

		

