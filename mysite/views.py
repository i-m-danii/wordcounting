from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
     return render(request, 'home.html' , {'name': 'i - m - danii'})

def  count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    list_lenght = len(word_list)
    dict = {}

    for word in word_list:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1


        return render(request, 'count.html', {'fulltext': data ,'len': list_lenght ,  'dict': dict.items()})

def contact(request):
    return HttpResponse('<h1>This is Contact page</h1>')

