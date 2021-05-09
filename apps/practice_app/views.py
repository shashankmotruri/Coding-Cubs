from django.shortcuts import render

# Create your views here.
from .models import practice

def view_data(request):
    value = request.GET.get('category')
    practicecontent = practice.objects.filter(category=value).values_list('id','category','question','testinputs','answersource')
    return render(request, 'pages/practice/view_data.html', {
        'content': practicecontent,
})