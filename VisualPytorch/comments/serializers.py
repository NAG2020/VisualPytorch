from rest_framework import serializers
from .models import Comments

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','title','context','time','pic')
