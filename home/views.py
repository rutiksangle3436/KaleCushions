from django.http import HttpResponse
from .models import Catogiries
from django.shortcuts import render, get_object_or_404
from django.http import Http404

def index(request):
	all_catogiries = Catogiries.objects.all().order_by('catogiry')
	context = {
		'all_catogiries':all_catogiries
	}
	return render(request, 'home/index.html', context)
	
def usingID(request,photo_cat):
	photos = get_object_or_404(Catogiries,catogiry=photo_cat)
	
	photo = Catogiries.objects.get(catogiry=photo_cat)
	all_photos = Catogiries.objects.all()	
	
	context = {'all_photos':all_photos,'item':photo}
	
	return render(request, 'home/404.html' , context)

