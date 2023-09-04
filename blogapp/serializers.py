from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"

class MainPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainPage
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"