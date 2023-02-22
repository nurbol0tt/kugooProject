from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework.views import APIView

from product.models import Product, Menu, Banner, TechniqueCategory, TypeCategory
from product.serializers import *


class ProductDetailView(APIView):

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializers = ProductSerializer(product)
        return Response(serializers.data)


class MenuListView(APIView):

    def get(self, request):
        product = Menu.objects.all()
        serializer = MenuSerializer(product, many=True)
        return Response(serializer.data)


class BannerFilterHome(APIView):

    def get(self, request):
        # banner = Banner.objects.filter(place_category=1)
        banner = Banner.objects.all()
        serializer = BannerFilterSerializer(banner, many=True)
        return Response(serializer.data)


class TechnicListView(APIView):

    def get(self, request):
        queryset = TechniqueCategory.objects.all()
        serializer = TechnicListSerializer(queryset, many=True)
        return Response(serializer.data)


class TypeCategoryList(APIView):

    def get(self, request):
        queryset = TypeCategory.objects.all()
        serializer = TypeCategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CartProductList(APIView):

    def get(self, request):
        queryset = Product.objects.all()
        serializer = CartProductSerializer(queryset, many=True)
        return Response(serializer.data)
