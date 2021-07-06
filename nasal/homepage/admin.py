from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Dog, Cat
from cows.models import Cattle, CommentonCattle
from dogs.models import Dogcomment
from cats.models import CommentonCat

# Admin class 
class CatAdmin(admin.ModelAdmin):
    fields = ('breed_name','country_origin','breed_type','body_type','brief','images','comment_id','popularity','danger','coat_pattern','color','temperament','lifespan','height','weight')
    list_display = ('breed_name','country_origin','temperament','appearance')
    list_editable = ('temperament','appearance')
    search_fields =('country_origin','breed_name')
    ordering = ['breed_name']
    list_filter = ('country_origin','popularity')

class DogAdmin(admin.ModelAdmin):
    list_display = ('breed_name','country_origin')
    search_fields =('country_origin','breed_name')
    ordering = ['breed_name']
    list_filter = ('country_origin','popularity')

# Register your models here.
admin.site.site_header='Breed.com'
admin.site.register(Dog,DogAdmin)
admin.site.register(Cat,CatAdmin)
admin.site.unregister(Group)
admin.site.register((Cattle,Dogcomment,CommentonCattle))
