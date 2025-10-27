from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def set_session(request):
    """session"""

    request.session["name"] = "xiaobai"
    request.session["id"] = 19
    responses = HttpResponse("set session")
    print(dict(request.session.items()))
    return responses

def get_session(request):
    """获取session"""
    responses = HttpResponse("get session")
    print(request.session)
    print(request.session.get("name"))
    print(request.session.get("id"))
    print(dict(request.session.items()))
    return responses

def del_session(request):
    """删除session"""
    responses = HttpResponse("del session")
    # request.session.clear() # 全部清空
    request.session.pop("name") # 删除不存在的会报错
    return responses