from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Comments
from .serializers import CommentSerializer
from rest_framework import permissions
import os
from VisualPytorch import settings
from django.http import FileResponse,StreamingHttpResponse
import json
from rest_framework.views import APIView
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

class CommentList(APIView):
    def get(self, request):
        comments_list = Comments.objects.all().values("id","title","context","time","pic");
        return Response(list(comments_list), status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request):
        #print(request.POST)
        try:
            pic = request.FILES['pic']
            data = {
                "title": request.POST["title"],
                "context": request.POST["context"],
                "pic": request.POST["title"] + pic.name,
            }
            save_path = "%s/usr_img/%s" % (settings.MEDIA_ROOT, request.POST["title"] + pic.name,)
            print(save_path)
            with open(save_path, "wb") as f:
                for content in pic.chunks():
                    f.write(content)
            f.close()
        except:
            data = {
                "title": request.POST["title"],
                "context": request.POST["context"],
                "pic": "default.jpg",
            }

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # data = {
        #     "title": request.data["title"],
        #     "context": json.dumps(request.data["context"])
        # }