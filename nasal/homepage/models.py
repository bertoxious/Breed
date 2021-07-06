from django.db import models

# Create your models here.
class Dog(models.Model):
    breed_name = models.CharField(max_length=200)
    country_origin = models.CharField(max_length=200)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    lifespan = models.CharField(max_length=100)
    brief = models.CharField(max_length=1000)
    images = models.ImageField()
    popularity = models.IntegerField()
    danger = models.IntegerField()
    temperament = models.CharField(max_length=200)

    def __str__(self):
        return self.breed_name

class Cat(models.Model):
    breed_name = models.CharField(max_length=200)
    country_origin = models.CharField(max_length=200)
    breed_type = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    brief = models.CharField(max_length=1000)
    images = models.ImageField()
    comment_id = models.IntegerField(unique=True)
    popularity = models.IntegerField()
    danger = models.IntegerField()
    coat_pattern = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    temperament = models.CharField(max_length=10000)
    lifespan = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    appearance = models.CharField(max_length=10000)
    def __str__(self):
        return self.breed_name

class Comment(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(default='monte@carlo.com')
    body = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return '{} commented on {} - at {}'.format(self.name,self.cat.breed_name,self.name)
