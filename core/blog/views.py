from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from blog.serializers import UserSerializer, UpdateUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
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
        try:
            return User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            raise Http404

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
