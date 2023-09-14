from django.shortcuts import render
from django.http import JsonResponse
import json
import logging
from pdb import set_trace


logging.basicConfig(level=logging.INFO)

# Create your views here.


def api_home(request, *args, **kwargs) -> dict:
    body = request.body
    data = {}
    try:
        data = json.loads(body)
        print(data)
    except:
        logging.exception("ERROR")
    # data["headers"] = request.headers
    return JsonResponse(data)
