from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product
from .producer import publish as rmqpublish
from .serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ViewSet):

	def list(self, request):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		rmqpublish()
		return Response(serializer.data)

	def create(self, request):
		serializer = ProductSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		#publish('product_created', serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def retrieve(self, request, pk=None):
		product = Product.objects.get(id=pk)
		serializer = ProductSerializer(product)
		return Response(serializer.data)

	def update(self, request, pk=None):
		product = Product.objects.get(id=pk)
		serializer = ProductSerializer(instance=product, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		#publish('product_updated', serializer.data)
		return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

	def destroy(self, request, pk=None):
		product = Product.objects.get(id=pk)
		product.delete()
		#publish('product_deleted', pk)
		return Response(status=status.HTTP_204_NO_CONTENT)