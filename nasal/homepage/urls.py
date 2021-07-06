from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name='homepage'),
    path('searched/',views.searched,name='searched-item'),
    path('detailed/<id>/',views.detailed,name='detailed-info'),
    path('about/',views.about,name='about'),
    path('newtypes/',views.newtypes,name='cat-types'),
    path('index/',views.index, name='index-page'),
    path('explore/',views.explore,name='explore'),
]