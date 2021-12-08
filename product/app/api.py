from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product

class ProductCreateApi(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteApi(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer