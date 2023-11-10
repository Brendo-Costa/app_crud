"""Serializer model for api app."""
from rest_framework.serializers import ModelSerializer
from .models import Blog




"""Blog serializer class"""
class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'