from django.http.response import HttpResponse

from django.shortcuts import render
from django.views.decorators.http import require_http_methods


# Create your views here.
@require_http_methods(["POST"])
def index(request):
    data = "<h5> OK! <h5>"
    # print(request)
    return HttpResponse(data, content_type="text/html")