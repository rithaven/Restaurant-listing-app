from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Restorent
# Create your views here.
def resto(request):
    restorent=Restorent.restorent()
    return render (request, 'restaurents.html',{"restorent":restorent})
def search_resto(request):
    if 'restorent' in request.GET and request.GET["restorent"]:
        search_term= request.GET.get("restorent")
        searched_restorents=Restorent.search_resto(search_term)

        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"locations":search_resto})
    else:
        message ="You haven't searched for anything , please write a correct location"
        return render(request,'serach.html',{"message": message})

def resto_location(request):
    restos=Restorent.restorent_location()
    return render(request,'location.html',{"restos":restos})
    