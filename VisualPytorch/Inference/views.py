from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Inference
from .serializers import InferenceSerializer
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
from .code.resnet18.resnet_inference import inference
# Create your views here.

class InferenceList(APIView):
    def get(self, request):
        inference_list = Inference.objects.all().values("id","pic");
        return Response(list(inference_list), status=status.HTTP_200_OK)
    @csrf_exempt
    def post(self, request):
        #print(request.POST)
        try:
            pic = request.FILES['pic']
            data = {
                "pic": pic.name,
            }
            save_path = "%s/inference_img/%s" % (settings.MEDIA_ROOT, pic.name,)
            pkl_path = "%s/pkls/" % (settings.MEDIA_ROOT)
            print(save_path)
            with open(save_path, "wb") as f:
                for content in pic.chunks():
                    f.write(content)
            f.close()
        except:
            data = {
                "pic": "nonepic.jpg",
            }
        serializer = InferenceSerializer(data=data)
        if serializer.is_valid():

            serializer.save()
            print(serializer.data["pic"])
            dic = inference(save_path,pkl_path)
            return Response(dic, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)