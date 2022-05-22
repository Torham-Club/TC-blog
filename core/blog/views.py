from django import dispatch
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from blog.models import Posts
from blog.serializers import PostCreateSerializer, UserSerializer, UpdateUserSerializer, UsersAdditionalInfoSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class UserUpdate(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    serializer_class = UpdateUserSerializer

    def get_object(self, user_pk):
        return get_object_or_404(User, pk=user_pk)

    def put(self, request):

        user_pk = request.user.pk
        user_data = self.get_object(user_pk)
        serializer = UpdateUserSerializer(
            instance=user_data,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200)


class CreateUsersAdditionalInfo(generics.GenericAPIView):

    serializer_class = UsersAdditionalInfoSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):

        user_pk = request.user.pk
        req_data = request.data
        req_data["user"] = user_pk

        serializer = UsersAdditionalInfoSerializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PostCreate(generics.CreateAPIView):
    
    queryset = Posts.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]
    
    # Set the author of the post.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

  

        