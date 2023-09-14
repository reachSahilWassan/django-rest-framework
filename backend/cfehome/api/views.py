from django.shortcuts import render
from django.http import JsonResponse
import json
import logging
from pdb import set_trace
from products.models import Products
from django.forms.models import model_to_dict


logging.basicConfig(level=logging.INFO)

# Create your views here.


def api_home(request, *args, **kwargs) -> dict:
    product_data = Products.objects.all().order_by("?").first()
    data = {}
    try:
        if product_data:
            data = model_to_dict(product_data)
    except:
        logging.exception("ERROR")
    # data["headers"] = request.headers
    return JsonResponse(data)
