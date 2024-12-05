from django.shortcuts import render

# Create your views here.

def biology(request):
    return render(request, 'biology.html')

def zoology(request):
    return render(request, 'zoology.html')

