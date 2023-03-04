from django.db.models import Min, OuterRef
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework.views import APIView

from product.models.misc_models import CatalogCategory, TypeCategory, Banner, Menu
from product.models.product_models import Product
from product.serializers import *


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


class TypeCategoryList(APIView):

    def get(self, request):
        queryset = TypeCategory.objects.annotate(
            min_price=models.Subquery(
                Product.objects.filter(
                    category__tech_category__title=OuterRef('title')
                ).order_by('new_price').values('new_price')[:1]
            )
        )
        serializer = TypeCategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CatalogCategoryListView(APIView):

    def get(self, request):
        queryset = CatalogCategory.objects.all()
        serializer = CatalogCategoryListSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductListView(APIView):

    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data)


class LikeView(APIView):

    def post(self, request, pk):
        post = get_object_or_404(Product, pk=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return Response(status=200)

