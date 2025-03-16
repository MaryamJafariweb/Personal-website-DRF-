from rest_framework import serializers
from .models import About


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('name', 'profession')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
