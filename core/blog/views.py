from django.contrib.auth.models import User
from blog.models import UsersAdditionalInfo, Posts, Comment
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from blog.serializers import (
    UserSerializer,
    UpdateUserSerializer,
    UsersAdditionalInfoSerializer,
    PostCreateSerializer,
    PostSerializer,
    CommentSerializer
)


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


class CreateAndUpdateUsersAdditionalInfo(generics.GenericAPIView):

    serializer_class = UsersAdditionalInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, user_pk):
        return get_object_or_404(UsersAdditionalInfo, user__pk=user_pk)

    def post(self, request):

        user_pk = request.user.pk
        req_data = request.data
        req_data["user"] = user_pk

        serializer = UsersAdditionalInfoSerializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 201)

    def put(self, request):

        user_pk = request.user.pk
        req_data = request.data
        req_data["user"] = user_pk

        user_data = self.get_object(user_pk)
        serializer = UsersAdditionalInfoSerializer(
            instance=user_data,
            data=req_data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200)


class DetailEditRemovePostAPI(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )

class PostCreate(generics.CreateAPIView):

    queryset = Posts.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    # Set the author of the post.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostList(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    

class CommentCreate(generics.CreateAPIView):
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
