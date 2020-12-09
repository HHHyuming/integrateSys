import random
from io import BytesIO

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw

from django.shortcuts import render, HttpResponse
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_center.models import User
from user_center.serializers import UserInfoSerializer
from utils.imgCode import Captcha
from utils.auth import encryption_password, decryption_password, TokenAuth
from utils.myResponse import myResponse
from itegrateSys import settings


class UserView(APIView):
    def get(self, request):
        user_queryset = User.objects.all()
        serializer = UserInfoSerializer(user_queryset, many=True)
        return myResponse(data=serializer.data).render()


@api_view(['POST'])
def user_login(request):
    request_params = request.data
    user_name = request_params.get('user_name')
    user_pwd = request_params.get('user_pwd')
    auth_user = User.objects.filter(username=user_name).first()
    if not auth_user:
        raise APIException('该用户不存在', code=2000)
    new_pwd = decryption_password(user_pwd)
    if auth_user.password == new_pwd:
        payload = {'username': user_name}
        token = TokenAuth().create_token(payload)
        return myResponse(data={'token': token}).render()
    return myResponse(code=2001, msg='用户名或密码错误!').render()


@api_view(['GET'])
def refresh_token(request):
    pass


@api_view(['GET'])
def test_api(request):
    return Response(b'TEST API IS OK', content_type='image/png')


@api_view(['GET'])
def get_code(request):
    captcha = Captcha()
    fp = captcha.make_captcha()

    io_data = fp.getvalue()
    # result = str(io_data, encoding='utf8')
    # print(f'这是IO数据{type(result)}')
    return HttpResponse(io_data, content_type="image/png")


@api_view(['POST'])
def register(request):
    request_params = request.data
    user_name = request_params.get('user_name')
    user_pwd = request_params.get('user_pwd')
    new_pwd = encryption_password(user_pwd).decode('utf8')
    user = User.objects.filter(username=user_name)
    if user:
        raise APIException('用户已存在')
    # User(username=user_name, password=new_pwd).save()
    serializer = UserInfoSerializer(data={'username': user_name, 'password': new_pwd}, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return myResponse(data=serializer.data)
