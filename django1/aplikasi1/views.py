from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'nama' : 'Selamat datang!',
    }
    return render(request, 'index.html', context)