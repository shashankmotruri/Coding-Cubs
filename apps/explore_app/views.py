from django.shortcuts import render, HttpResponse
from .models import explore
from .forms import Feedbackform


def read_article(request):
    id_from_url = request.GET.get('id')
    content = explore.objects.filter(id=id_from_url).values()
    return render(request, 'pages/explore/read_article.html',{
        'content': content[0],
    })

def feedback(request):
    if request.method == 'GET':
        form = Feedbackform
        return render(request,'pages/explore/feedbackpage.html',{
            'form':form,
        })

    if request.method == 'POST':
        form = Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("SAVED")

def favourites(request):
    if request.method == 'GET':
        id_from_url = request.GET.get('id2')
        content = explore.objects.filter(id=id_from_url).values()
        content = content[0]
        topic = content['topic']
        category = content['category']
        source = content['source']
        description = content['description']
        return render(request, 'pages/explore/favourites.html', {
            'topic': topic,
            'category': category,
            'source' : source,
            'description' : description,
        })

    elif request.method == 'POST' :
        return HttpResponse("Works")

def view_info(request):
    value = request.GET.get('category')
    content = explore.objects.filter(category=value).values_list('id','topic','category','source','description')
    return render(request, 'pages/explore/view_info.html', {
        'content': content,
})

