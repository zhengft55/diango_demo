from http.client import responses

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def set_cookie(request):
    """设置cookie"""
    responses = HttpResponse("set cookie")
    responses.set_cookie("name", "xiaoming", max_age=30, path="/mycookies/")
    return responses

def get_cookie(request):
    """获取ookie"""
    print(request.COOKIES)
    print(request.COOKIES.get("name"))
    return HttpResponse("get cookie")

def del_cookie(request):
    """删除ookie"""
    responses = HttpResponse("del cookie")
    responses.delete_cookie("name")
    return responses