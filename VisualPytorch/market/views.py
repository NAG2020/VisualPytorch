from django.shortcuts import render
from django.views.generic import View
from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from NeuralNetwork.models import Network
from BaseApiView.views import APIView
from .permissions import ModelMarket
from NeuralNetwork.serializers import NetworkSerializer
from django.core.paginator import Paginator
# Create your views here.

class modelList(APIView):
    permission_classes = (ModelMarket,)

    def get(self, request):
        pagesize = request.GET['pagesize']
        if pagesize:
            pagesize = int(pagesize)
        else:
            pagesize = 10
        
        page = request.GET['page']
        if page:
            page = int(page)
        else:
            page = 1
        
        network_list = Network.objects.filter(and_(shared=True, sharable=True)).values('name', 'description', 'png')
        paginator = Paginator(network_list, pagesize)

        # 获得指定页的列表
        page_network_list = paginator.page(page)
        page_num = paginator.num_pages

        if page_network_list.has_next():
            next_page = page + 1
        else:
            next_page=page
        
        if page_network_list.has_previous():
            previous_page = page - 1
        else:
            previous_page = page

        data = {
            'networklist': page_network_list,
            'page_num': range(1, page_num),
            'cur_page': page,
            'next_page': next_page,
            'previous_page': previous_page
        }
        return Response(data=data, content_type='application/json', status=status.HTTP_200_OK)
    

class modelDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Network.objects.get(pk=pk)
        except Network.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        network = self.get_object(pk)
        serializer = NetworkSerializer(network)
        return Response(serializer.data)

    def post(self, request, pk):
        network = self.get_object(pk)
        data = {
            "name": network.name,
			"creator": request.user.id,
            "structure": network.structure,
            "description": network.description,
            "png": network.png,
            "sharable": False,   # 市场的模型不允许共享
            "shared": False
        }
        serializer = NetworkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
