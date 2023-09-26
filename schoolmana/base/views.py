from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'basic.html')

def login(request):
    return render(request, 'loginpage.html')

def studentdashb(request):
    return render(request, 'studentdash.html')