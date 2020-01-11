from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image
# Create your views here.
def resto(request):
    restaurent=Resto.restaurent()
    return render (request, 'restaurents.html',{"restaurent":restaurent})
