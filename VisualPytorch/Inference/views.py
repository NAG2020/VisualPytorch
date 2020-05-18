from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Inference
from .serializers import InferenceSerializer
from rest_framework import permissions
import os
from VisualPytorch import settings
from django.http import FileResponse, StreamingHttpResponse
import json
from rest_framework.views import APIView
import time

from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .code.resnet18.resnet_inference import resnet18
from .code.dcgan.gan_inference import gcgan
from .code.faster_rcnn.detection_demo import faster_rcnn
from .code.unet.portrait_inference import unet
from .code.resnet101.seg_demo import resnet101

# Create your views here.

class Resnet18(APIView):
    @csrf_exempt
    def post(self, request):
        # print(request.POST)
        try:
            pic = request.FILES['pic']
            data = {
                "pic": pic.name,
            }
            save_path = "%s/inference_img/%s" % (settings.MEDIA_ROOT, pic.name,)
            pkl_path = "%s/pkls/" % (settings.MEDIA_ROOT)
            # print(save_path)
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
            # print(serializer.data["pic"])
            dic = resnet18(save_path, pkl_path)
            return Response(dic, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Dcgan(APIView):
    @csrf_exempt
    def post(self, request):
        # print(request.data)
        try:
            # print(request.data["num_img"] + " " + request.data["nrow"] + " " + request.data["noise_continue"])
            num_img = request.data["num_img"]
            nrow = request.data["nrow"]
            noise_continue = request.data["noise_continue"]

            save_path = "%s/inference_img/%s" % (settings.MEDIA_ROOT, "dcgan-gene"+str(time.time())+".jpg",)
            pkl_path = "%s/pkls/" % (settings.MEDIA_ROOT)
            print(save_path)
            dic = gcgan(save_path, pkl_path, num_img, nrow, noise_continue)
            return Response(dic, status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Frcnn(APIView):
    @csrf_exempt
    def post(self, request):
        # print(request.POST)
        try:
            pic = request.FILES['pic']
            data = {
                "pic": pic.name,
            }
            save_path = "%s/inference_img/%s" % (settings.MEDIA_ROOT, pic.name,)
            pkl_path = "%s/pkls/" % (settings.MEDIA_ROOT)
            # print(save_path)
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
            # print(serializer.data["pic"])
            dic = faster_rcnn(save_path, pkl_path)
            return Response(dic, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Unet(APIView):
    @csrf_exempt
    def post(self, request):
        # print(request.POST)
        try:
            pic = request.FILES['pic']
            data = {
                "pic": pic.name,
            }
            save_path = "%s/inference_img/%s" % (settings.MEDIA_ROOT, pic.name,)
            pkl_path = "%s/pkls/" % (settings.MEDIA_ROOT)
            # print(save_path)
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
            # print(serializer.data["pic"])
            dic = unet(save_path, pkl_path)
            dic["raw"] = save_path
            return Response(dic, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Resnet101(APIView):
    @csrf_exempt
    def post(self, request):
        # print(request.POST)
        try:
            pic = request.FILES['pic']
            data = {
                "pic": pic.name,
            }
            save_path = "%s/inference_img/%s" % (settings.MEDIA_ROOT, pic.name,)
            pkl_path = "%s/pkls/" % (settings.MEDIA_ROOT)
            # print(save_path)
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
            # print(serializer.data["pic"])
            dic = resnet101(save_path, pkl_path)
            dic["raw"] = save_path
            return Response(dic, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)