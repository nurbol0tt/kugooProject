from rest_framework import serializers

from blogpost.models import *


class QuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswer
        fields = ('id', 'question', 'answer')


class ServiceCenterSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceCenter
        fields = ('id', 'title', 'number', 'mode')


class StorePointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = StorePoints
        fields = ('id', 'title', 'number')


class MediaBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaBlog
        fields = ('id', 'image')


class BLogListSerializer(serializers.ModelSerializer):
    inside_photo = MediaBlogSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'external_photo', 'inside_photo', 'date_created', 'description', 'views')


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('id', 'title', 'video_file')


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('id', 'title', 'description', 'image')
