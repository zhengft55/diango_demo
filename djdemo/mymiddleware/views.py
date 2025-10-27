from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class MiddlewareView(View):

    # 可以定义其他方法，仅用于公共数据，外界不可访问
    def other(self):
        pass

    def post(self, request):
        return HttpResponse("user -> post")

    def get(self, request):
        return HttpResponse("user -> get")