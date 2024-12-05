from django.shortcuts import render

# Create your views here.

def audi(request):
    return render(request, 'audi.html')