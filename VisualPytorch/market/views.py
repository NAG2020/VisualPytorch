from django.shortcuts import render
from django.views.generic import View
from rest_framework import permissions
from rest_framework.response import Response
from NeuralNetwork.models import Network
from BaseApiView.views import APIView
from .permissions import ModelMarket
# Create your views here.

class modelList(APIView):
    permission_classes = (ModelMarket,)

    def get(self, request):
        network_list = Network.objects.filter(shared=True).values('description', 'png')
        return Response(list(network_list), status=status.HTTP_200_OK)
    