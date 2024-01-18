from typing import Any

from django.http import HttpRequest
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_home(request: HttpRequest, *args: Any, **kwargs: Any):
    """
    DRF API View
    """
    data = {}

    instance: Product = Product.objects.all().order_by("?").first()
    if instance:
        # data = model_to_dict(instance, fields=["id", "title", "price", "sale_price"])
        data = ProductSerializer(instance).data

    return Response(data)
