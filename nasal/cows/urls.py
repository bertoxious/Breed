from django.urls import path 
from . import views 
urlpatterns = [
    path('most-popular-dairy-cattle-breeds',views.dairycows,name='dairy-breeds'),
    path('most-milk-producing-cows-of-India',views.indiandairycows,name='indian-dairy-cows'),
    path('popular-dairy-breeds-of-America',views.americandairycows,name='american-dairy-cows'),
    path('most-common-cattle-breeds',views.commondairycows,name='most-common-cattle-breeds'),
    path('cattle-breeds/',views.cowtypes,name='cow-types'),
    path('cattle-detailed/<int:id>/',views.cowsdetailed,name='cows-detailed-info'),
    path('cow-comment-section/<int:id>/comment',views.addcowcomment,name='add-cow-comment'),
]