from django.shortcuts import render, HttpResponse

def dashboard(request):
    return render(request, 'dashboard.html')

def index(request):
    context = {}
    return render(request, 'pages/index.html')

def home(request):
    context = {"home_page" : "active"}
    return render(request, 'pages/home.html',context)

def explore_page(request):
    context = {"explore_page" : "active"}
    return render(request, 'pages/explore/explore_page.html',context)

def learn(request):
    context = {"learn_page" : "active"}
    return render(request, 'pages/learn',context)

def practice_page(request):
    context = {"practice_page" : "active"}
    return render(request, 'pages/practice/practice.html',context)
