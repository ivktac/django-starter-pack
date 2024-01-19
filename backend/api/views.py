from typing import Any

from rest_framework.views import Request

from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def api_home(request: Request, *args: Any, **kwargs: Any):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.save()
        return Response(serializer.data)
    return Response({"message": "Invalid Data"}, status=400)
