import json
from telnetlib import STATUS

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.
from django.http.response import HttpResponse, JsonResponse

from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods


# Create your views here.
# @require_http_methods(["POST"])
def index(request):
    data = "<h1> OK! goods <h1>"
    print(request.GET)
    # 获取单个
    print(request.GET.get('name'))  # 取不到为 None
    print(request.GET['psd'])  # 不要用，取不到报错

    # 获取多个 结果是列表
    print(request.GET.getlist('lce'))
    return HttpResponse(data, content_type="text/html")


def index2(request):
    data = "<h1> OK! POST <h1>"
    print(request.GET)
    print(request.POST)  # 只能获取post请求体， 不能获取put/patch
    print(request.POST.get('long1'))  # 取不到为 None
    print(request.POST.get('long2', 'kong'))

    print(request.POST.getlist('long1'))
    return HttpResponse(data, content_type="text/html")


def index3(request):
    print(request.body)
    # 获取put/patch 等请求 的请求体
    data = json.loads(request.body)
    print(data)

    # 获取原生请求头
    print("META为：", request.META)
    # 获取http请求头
    print("headers为：", request.headers)
    print("headers为：", request.headers.get(""))

    # 获取文件 只能接收post请求的文件
    print("文件为：", request.FILES)
    print("文件为：", request.FILES.get(""))
    return HttpResponse(data, content_type="text/html")


def index5(request):
    # 响应html
    data = "<h1> OK! html <h1>"
    # return HttpResponse(content=data, content_type="text/html",status=201,headers={"token":"123"})
    return HttpResponse(data, content_type="text/html")


def index6(request):
    # 响应json
    data = [{
        "id": 1,
        "name": "tom"
    }]
    json_data = json.dumps(data)
    # return HttpResponse(content=data, content_type="text/html",status=201,headers={"token":"123"})
    return HttpResponse(json_data, content_type="text/json")


def index7(request):
    # 直接返回json
    data = {
        "id": 1,
        "name": "tom7"
    }

    return JsonResponse(data)

    # 并不直接支持列表转换为json 需要关闭安全参数
    # data = [{
    #     "id": 1,
    #     "name": "tom7"
    # }]

    # return JsonResponse(data, safe=False)


def index8(request):
    # 返回图片

    # with open("./goods/133.png", "rb") as f:
    #     img = f.read()
    # return HttpResponse(content=img, content_type="image/png")

    # 返回压缩包

    with open("./goods/133.zip", "rb") as f:
        zip = f.read()
    return HttpResponse(content=zip, content_type="application/x-gzip")


def index9(request):
    # 自定义响应头

    response = HttpResponse("ok!!!!")
    response["company"] = "dhc sb upnock sb"
    return response


def index10(request):
    # 跳转/重定向

    # response = HttpResponse(status=302)
    # response["Location"] = "https://www.baidu.com/index.html"
    # return response

    # 临时重定向  上下等价
    return HttpResponseRedirect("https://www.baidu.com/index.html")


def index11(request):
    # 站内跳转
    # reverse("goods:index11") 的作用是根据路由别名 "namespace:name" 反解析出对应的URL路径，例如 "/goods/index11/"
    # 一般配合 redirect 或 HttpResponseRedirect 用于重定向站内 URL
    # 例如：redirect(reverse("goods:index11"))

    # return redirect("/goods/index7/")

    url = reverse("goods:index7")
    return redirect(url)
