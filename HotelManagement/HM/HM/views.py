from django.shortcuts import render

def SleepyHub(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def home(request):
    return render(request,"home.html")
def registrationPage(request):
    return render(request,"register.html")
