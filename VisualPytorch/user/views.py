from django.shortcuts import render
from .serializers import UserSerializer
from BaseApiView.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import User
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework import permissions
from VisualPytorch import settings
# from itsdangerous import TimedJSONWebSignatureSerializer as ts

# Create your views here.

class UserRegister(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 注册时签发一个token来自动登录
            payload = jwt_payload_handler(serializer.instance)
            token = jwt_encode_handler(payload)
            res = serializer.data
            res["token"] = token
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfo(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class EmailVariyView(APIView):

    def get(self, request):

        # todo 取出连接中的token
        recieve_token = request.query_params.get('token')
        print('===========EmailVariy===========')

        # todo 校验token是否为空
        if not recieve_token:
            return Response({'err_msg':'缺少token参数'},status=400)
        # todo 将token进行解密

        # 1.生成ts_obj
        ts_obj = ts(settings.SECRET_KEY)
        # 2.将token拿过来解析
        data = ts_obj.loads(recieve_token)
        print('解码过后的token数据')
        print(data)
        # 3.将id和email一起获取对象
        username = data['username']
        email = data['email']

        user_obj = User.objects.get(username=username,email=email)
        # todo 验证一下
        # todo 设置激活的字段
        user_obj.is_active = True
        user_obj.save()
        return Response('OK')