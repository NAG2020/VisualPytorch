from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Comments
from .serializers import CommentSerializer
from rest_framework import permissions
import os
from django.conf import settings
from django.http import FileResponse,StreamingHttpResponse
import json
from rest_framework.views import APIView
import time
from django.db.models import Q
# Create your views here.
class CommentList(APIView):
    def get(self, request):
        comments_list = Comments.objects.all().values("id","title","context","time");
        return Response(list(comments_list), status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            "title": request.data["title"],
            "context": json.dumps(request.data["context"])
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
