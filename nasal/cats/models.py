from django.db import models
from homepage.models import Cat

class CommentonCat(models.Model):
    cat = models.ForeignKey(Cat,related_name='cat_comments', on_delete=models.CASCADE,db_column = 'cat',blank=True,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(default='monte@carlo.com')
    body = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return '{} commented on {} - at {}'.format(self.name,self.cat,self.date_added)
