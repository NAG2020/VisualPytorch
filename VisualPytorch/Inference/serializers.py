from rest_framework import serializers
from .models import Inference

class InferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inference
        fields = ('id','pic')
