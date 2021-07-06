from django.urls import path 
from cats import views 
urlpatterns = [
    path('cat-comment-section/<int:id>/comment',views.addcomment,name='add-comment'),
    path('largest-cat-breeds/',views.largestcats,name='largest-cats'),
    path('beautiful-cat-breeds/',views.beautifulcats,name='beautiful-cats'),
    path('popular-cat-breeds/',views.popularcats,name='most-popular-cats'),
    path('fluffiest-cat-breeds/',views.fluffiestcats,name='fluffiest-cats'),
    path('dangerous-cat-breeds/',views.dangerouscats,name='dangerous-cats'),
]