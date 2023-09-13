from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def api_view(request) -> dict:
    return JsonResponse({"message": "api worked"})
