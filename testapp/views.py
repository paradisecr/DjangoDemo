from django.shortcuts import render
from django.shortcuts import HttpResponse
from testapp import models
# Create your views here.

def test(request):
    return render(request, "test.html",)
    # return HttpResponse("Test, here is Rui Cao.")

def list(request):
    # data_list = [
    #     {"user" : "曹睿", "level" : "最强王者" },
    #     {"user" : "骨戒", "level" : "不屈黄铜" },
    # ]
    data_list = models.UserInfo.objects.all()
    return render(request, "list.html", {"data" : data_list})

def addUser(request):
    userName = request.GET.get("userName", None)
    level = request.GET.get("level", None)
    models.UserInfo.objects.create(user = userName, level = level)
    return HttpResponse(userName + ":" + level)
