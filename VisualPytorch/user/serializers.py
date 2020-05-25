from rest_framework import serializers
from .models import User
from django.core.mail import send_mail
from VisualPytorch import settings
from itsdangerous import TimedJSONWebSignatureSerializer as ts

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "password", "username", "email", "is_active", "is_staff")

    # 重写serializer的create方法，该方法将在serializer.save()时被调用，此处为直接注册用户
    def create(self, validated_data):
        ts_obj = ts(settings.SECRET_KEY)
        # 加密
        token = ts_obj.dumps(validated_data).decode()
        url = 'http://114.115.148.27:80/api/user/email/?token='+token
        # todo 发送邮件
        url_string = '欢迎使用VisualPytorch,请点击<a href=' + url + '>链接</a>确认注册'
        # 邮件主题
        subject = 'VisualPytorch激活邮件'
        # 邮件信息，正文部分
        message = '欢迎'
        # 发送者，直接从配置文件中导入上面配置的发送者
        sender = settings.EMAIL_FROM
        # 接收者的邮箱，是一个列表，这里是前端用户注册时传过来的 email
        receiver = [validated_data["email"],]
        # html结构的信息，其中包含了加密后的用户信息token
        html_message = url_string
        # 调用Django发送邮件的方法，这里传了5个参数

        send_mail(subject, message, sender, receiver, html_message=html_message)
        return User.objects.create_user(**validated_data)
