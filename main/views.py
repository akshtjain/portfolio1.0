from django.shortcuts import render
from django.conf import settings


def index(request):
    context = {
        "name" : settings.DATA["NAME"],
        "aboutme" : settings.DATA["ABOUTME"]
    }
    return render(request, 'main\index.html', context)

def projects(request):
    context = {
        "projects" : settings.DATA["PROJECTS"]
    }
    return render(request, 'main\projects.html',context)

def languages(request):
    context = {
        "languages" : settings.DATA["LANGUAGES"]
    }
    return render(request, 'main\languages.html', context)