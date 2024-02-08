from django.shortcuts import render
from django.http import HttpResponse
from .models import Data

# Create your views here.
# Create your views here.
"""
def home(request):
    msg="<h1>Welcome to django</h1>"
    return HttpResponse(msg)
    
def home(request):
    return render(request,"home.html",{'Name':'Pavi'})
"""
def home(request):
    return render(request,"home.html")
def product(request):
    mobile=int(request.GET["mobile"])
    keyboard=int(request.GET["keyboard"])
    monitor=int(request.GET["monitor"])
    price=mobile+keyboard+monitor
    return render(request,"Result.html",{'Price':price})
def home_page(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        obj=Data()
        obj.Name=name
        obj.Mobile=mobile
        obj.save()
        mydata=Data.objects.all()    
    return render(request,'User_reg.html')

def result(request):
    password=request.GET['password']
    if(password=="Admin"):
        mydata=Data.objects.all()
        return render(request,'User_details.html',{'Data':mydata})
    else:
        print("Invalid password")
    