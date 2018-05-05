from django.shortcuts import render

from .models import AppOs

def home(request):
    AppOss = AppOs.objects.all()
    return render(request, 'index.html', {'AppOss': AppOss})

def app(request, id):
    app = AppOs.objects.get(id=id)
    return render(request, 'index.html', {'app': app})
