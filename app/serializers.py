from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ReservationModel
        fields = '__all__'

class RatesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = RatesModel
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ContactModel
        fields = '__all__'