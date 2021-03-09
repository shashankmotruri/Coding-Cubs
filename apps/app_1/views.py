from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')


def index(request):
    context = {}
    return render(request, 'pages/index.html')

def home(request):
    context = {"home_page" : "active"}
    return render(request, 'pages/home.html',context)

def explore(request):
    context = {"explore_page" : "active"}
    return render(request, 'pages/explore.html',context)

def learn(request):
    context = {"learn_page" : "active"}
    return render(request, 'pages/learn.html',context)

def practice(request):
    context = {"practice_page" : "active"}
    return render(request, 'pages/practice.html',context)

def discuss(request):
    context = {"discuss_page" : "active"}
    return render(request, 'pages/discuss.html',context)
