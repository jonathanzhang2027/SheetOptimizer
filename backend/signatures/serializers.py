from rest_framework import serializers
from .models import Signature, MeritSheet

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = '__all__'


class MeritSheetSerializer(serializers.ModelSerializer):
    # date = serializers.DateField(input_formats=['%m/%d/%Y'], required=True)  # Accept MM/DD/YYYY

    class Meta:
        model = MeritSheet
        fields = '__all__'
