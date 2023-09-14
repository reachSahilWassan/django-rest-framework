from django.shortcuts import render
from django.http import JsonResponse
import json
import logging
from pdb import set_trace
from products.models import Products
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer

from products.serializers import ProductSerializer


logging.basicConfig(level=logging.INFO)

# Create your views here.


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs) -> dict:
    """DRF API View"""

    product_data = Products.objects.all().order_by("?").first()
    data = {}

    if product_data:
        # data = model_to_dict(product_data)
        data = ProductSerializer(product_data).data
    # data["headers"] = request.headers
    return Response(data)
