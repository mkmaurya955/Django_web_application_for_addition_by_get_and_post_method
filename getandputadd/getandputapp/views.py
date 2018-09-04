from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def get_input(request):
    return render(request,'getinput.html')
def post_input(request):
    return render(request,'postinput.html')
def add(request):
    if request.method=='GET':
        try:
            a=request.GET['t1']
            x=int(a)
            b=request.GET['t2']
            y=int(b)
            z=x+y
            return HttpResponse("<html><body bgcolor=red><h1>Sum is:"+str(z)+ "</h1></body></html>")
        except(ValueError):
            return HttpResponse("Invalid input")
    else:
        try:
            a=request.POST['t1']
            x=int(a)
            b=request.POST['t2']
            y=int(b)
            z=x+y
            return HttpResponse("<html><body><h1>Sum is:"+str(z)+"</h1></body></html>")
        except(ValueError):
            return HttpResponse("Invalid Input")