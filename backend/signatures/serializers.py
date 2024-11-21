from rest_framework import serializers
from .models import Signature, MeritSheet

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = '__all__'

class MeritSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeritSheet
        fields = '__all__'
