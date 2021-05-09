from django.shortcuts import render
from .models import quiz

def take_quiz(request):
    results=quiz.objects.all()
    return render(request, 'pages/quiz.html', {"quiz": results})


