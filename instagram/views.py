from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Profile, Comments


# Create your views here.

def index(request):

    title = 'Instaclone'
    return render(request, 'index.html', {'title':title})

def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
