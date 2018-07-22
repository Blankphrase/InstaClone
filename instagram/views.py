from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Profile, Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):

    title = 'Instaclone'
    return render(request, 'index.html', {'title':title})

def profile(request, username):
    title = "InstaClone | Profile"
    profile = User.objects.get(username=username)

    try :
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)

    images = Image.get_profile_pic(profile.id)
    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'images':images})

def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
