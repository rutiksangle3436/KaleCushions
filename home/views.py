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
	

def contactus(request):
	context = {'all_photos':"All data"}
	return render(request, 'home/contactus.html', context)
