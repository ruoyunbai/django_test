from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return HttpResponse("HELLO WORLD")
def runoob(request):
    views_list=["菜鸟教程1","菜鸟教程2","菜鸟教程3"]
    return render(request,"runoob.html",{"views_list":views_list})
