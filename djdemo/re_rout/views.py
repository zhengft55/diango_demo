from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """获取ookie"""

    return HttpResponse("ok")


def info(request, id):
    """获取ookie"""

    return HttpResponse(f"id={id}的资料")

def goods(request, cat, dog):
    """获取ookie"""

    return HttpResponse(f"cat={cat}, dog = {dog}的资料")