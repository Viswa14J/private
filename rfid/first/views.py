from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def read(request):
    return render(request,'read.html')
def read1(request):
    return render(request,'read1.html',{'correct'})
def read1(request):
    return render(request,'read1.html',{'outofrange'})
def read1(request):
    return render(request,'read1.html',{'alert'})
def read1(request):
    return render(request,'read1.html',{'expired'})
def signin(request):
    return render(request,'signin.html')
def signup(request):
    return render(request,'signup.html')
def write(request):
    return render(request,'write.html')
def write2(request):
    return render(request,'write2.html')
def track(request):
    return render(request,'track.html')

# Create your views here.
