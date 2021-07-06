from django.urls import path 
from . import views 
urlpatterns = [
    path('most-popular-dogs/',views.topten,name='most-popular-dogs'),
    path('dangerous-dogs/',views.newten,name='top-ten-dangerous-dogs'),
    path('easy-to-train-dogs/',views.easy,name='easy-to-train-dogs'),
    path('largest-dogs',views.largestdogs,name='largest-dogs'),
    path('swimmer-dogs',views.swimmerdogs,name='swimmer-dogs'),
    path('dog-breeds/',views.dogtypes,name='dog-types'),
    path('dogs-detailed/<id>/',views.dogsdetailed,name='dogs-detailed-info'),
    path('dogs-detailed/<id>/add-dog-comment/',views.adddogcomment,name='add-dog-comment'),
]