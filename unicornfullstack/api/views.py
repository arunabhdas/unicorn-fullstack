from rest_framework import viewsets
from rest_framework.utils import serializer_helpers
from .serializers import ProductSerializer
from core.models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

def getCustomRoutes(request):
    routes = [
        {
            'Endpoint': '/products/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of products'
        },
        {
            'Endpoint': '/products/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product'
        },
        {
            'Endpoint': '/products/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new product with data sent in post request'
        },
        {
            'Endpoint': '/products/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing product'
        },
    ]
    return JsonResponse(routes, safe=False)