from django.shortcuts import render

# Create your views here.

def hotal(request):
    return render(request,'hotal.html')

def registration(request):
    return render(request,'registration.html')
