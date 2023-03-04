from rest_framework.response import Response

from rest_framework.views import APIView

from blogpost.serialziers import *


class QuestionAnswerListView(APIView):

    def get(self, request):
        queryset = QuestionAnswer.objects.all()
        serializer = QuestionAnswerSerializer(queryset, many=True)
        return Response(serializer.data)


class ServiceCenterListView(APIView):

    def get(self, request):
        queryset = ServiceCenter.objects.all()
        serializer = ServiceCenterSerializer(queryset, many=True)
        return Response(serializer.data)


class StorePointsListView(APIView):

    def get(self, request):
        queryset = StorePoints.objects.all()
        serializer = StorePointsSerializer(queryset, many=True)
        return Response(serializer.data)


class BLogListView(APIView):

    def get(self, request):
        queryset = BlogPost.objects.all()
        serializer = BLogListSerializer(queryset, many=True)
        return Response(serializer.data)


class VideoListView(APIView):

    def get(self, request):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)


class OfferListView(APIView):

    def get(self, request, pk):
        queryset = Offer.objects.filter(category=pk)
        print(queryset)
        serializer = OfferSerializer(queryset, many=True)
        return Response(serializer.data)
