from django.shortcuts import render
from django.http import JsonResponse
import json
import logging
from pdb import set_trace
from products.models import Products
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

logging.basicConfig(level=logging.INFO)

# Create your views here.


@api_view(["POST"])
def api_home(request, *args, **kwargs) -> dict:
    """DRF API View"""

    serializer = ProductSerializer(data=request.data)
    # product_data = Products.objects.all().order_by("?").first()
    data = {}
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        data = serializer.data
        return Response(data)
    


    # if product_data:
    #     # data = model_to_dict(product_data)
    #     data = ProductSerializer(product_data).data
    # return Response(data)
    # return JsonResponse(data)
