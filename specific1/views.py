from django.shortcuts import render

# Create your views here.

def skoda(request):
    return render(request, 'skoda.html')