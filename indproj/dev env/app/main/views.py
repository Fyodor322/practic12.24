from django.shortcuts import render

def index(request):
    context = {
        'tatle': 'Home',
        'content': 'Главная страница'
    }
    return render(request, 'main/index.html', context)
