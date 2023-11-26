from django.shortcuts import render

# Create your views here.

def login(request):
    d={'name':'Mr.chatta lokesh'}
    return render(request,'login.html',d)