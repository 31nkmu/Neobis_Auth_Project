from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from applications.account.serializers import RegisterSerializer, ForgotPasswordSerializer, \
    ForgotPasswordConfirmSerializer, RegisterBeginSerializer

User = get_user_model()


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    @swagger_auto_schema(tags=['register'], request_body=RegisterSerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RegisterBeginAPIView(APIView):
    @swagger_auto_schema(request_body=RegisterBeginSerializer, tags=['register'])
    def post(self, request):
        serializer = RegisterBeginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response({'msg': 'Вам отправили ссылку для дальнейшей регитрации'}, status=status.HTTP_200_OK)


class ActivateAPIView(APIView):
    @swagger_auto_schema(tags=['register'])
    def get(self, request, activation_code):
        user = User.objects.filter(activation_code=activation_code).first()
        if not user:
            return Response({'msg': 'Неверный код активации'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.activation_code = ''
        user.save(update_fields=('is_active', 'activation_code'))
        return Response({'msg': 'Ваш аккаунт успешно активирован'}, status=status.HTTP_200_OK)


class ForgotPasswordAPIVIew(APIView):
    @swagger_auto_schema(request_body=ForgotPasswordSerializer, tags=['forgot password'])
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response({'msg': 'Вам отправили код активации'}, status=status.HTTP_200_OK)


class ForgotPasswordConfirmAPIView(APIView):
    @swagger_auto_schema(request_body=ForgotPasswordConfirmSerializer, tags=['forgot password'])
    def post(self, request):
        serializer = ForgotPasswordConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.change_password()
        return Response({'msg': 'Ваш пароль успешно изменен'}, status=status.HTTP_200_OK)
