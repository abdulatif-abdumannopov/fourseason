from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = PostModel
        fields = '__all__'
