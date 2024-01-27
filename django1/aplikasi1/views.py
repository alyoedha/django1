from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'nama' : 'Hello world!',
    }
    return render(request, 'index.html', context)