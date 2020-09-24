from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {'a':1}
    return render(request, 'index.html', context)

def hotel(request):
    context = {'a':1}
    return render(request, 'hotel.html', context)

def vr(request):
    context = {'a':1}
    return render(request, 'vr.html', context)

def display(request):
    context = {'a':1}
    return render(request, 'display.html', context)

def leisure(request):
    context = {'a':1}
    return render(request, 'leisure.html', context)

def show(request):
    context = {'a':1}
    return render(request, 'show.html', context)

def video(request):
    context = {'a':1}
    return render(request, 'video.html', context)

def tour(request):
    context = {'a':1}
    return render(request, 'tour.html', context)

def login(request):
    context = {'a':1}
    return render(request, 'login.html', context)