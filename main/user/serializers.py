from rest_framework import serializers
from .models import UserLogin

class userLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = '__all__'