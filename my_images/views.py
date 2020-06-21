from django.shortcuts import render
from .models import *

# Create your views here.
def Home(request):
    images = Image.objects.all()
    cats =Category.objects.all()
    data = {'images':images,'cats':cats}
    return render(request,'my_images/home.html',data)

def Category_Page(request,cid):

    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    images = Image.objects.filter(cat=category)
    data = {'images': images, 'cats': cats}
    return render(request, 'my_images/home.html', data)
