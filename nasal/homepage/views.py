from django.shortcuts import render
from .models import Cat, Dog 
from cows.models import Cattle

# Create your views here.
def searched(request):
    if request.method == "POST":
        category = request.POST.get('retro',False)
        if category == 'Dogs':
            searched = request.POST['searched']
            breeds = Dog.objects.filter(breed_name__contains=searched)
            return render(request,'dogs/searched.html',{'searched':searched,'breeds':breeds})
        elif category == "Cows":
            searched = request.POST['searched']
            breeds = Cattle.objects.filter(breed_name__contains=searched)
            return render(request,'cows/searched.html',{'searched':searched,'breeds':breeds})
        elif category == "Cats":
            searched = request.POST['searched']
            breeds = Cat.objects.filter(breed_name__contains=searched)
            return render(request,'homepage/searched.html',{'searched':searched,'breeds':breeds})
        return render(request,'homepage/index.html')
def detailed(request,id):
    searched = Cat.objects.get(pk=id)
    return render(request,'homepage/detailed.html',{'searched':searched})

def about(request):
    return render(request,'homepage/about.html')

def newtypes(request):
    all_cats = Cat.objects.all
    return render(request,'homepage/newtypes.html',{'all':all_cats})

def index(request):
    return render(request,'homepage/index.html')

def explore(request):
    return render(request,'homepage/explore.html')

def newnavigation(request):
    category = request.GET["retro"]
    if category == 'Dogs':
        searched = request.POST['searched']
        breeds = Dog.objects.filter(breed_name__contains=searched)
        return render(request,'dogs/dogtypes.html')
    elif category == 'Cats':
        searched = request.POST['searched']
        breeds = Cat.objects.filter(breed_name__contains=searched)
        return render(request,'cats/cattypes.html')