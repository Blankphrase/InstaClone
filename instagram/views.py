from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
# from .models import


# Create your views here.

def index(request):

    title = 'Instaclone'
    return render(request, 'index.html', {'title':title})
