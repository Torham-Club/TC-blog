from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import UsersAdditionalInfo, Posts


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')


class UsersAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersAdditionalInfo
        fields = ('user', 'bio', 'profile_picture')

        def create(self, validated_data):
            user_info = UsersAdditionalInfo(**validated_data)
            user_info.save()
            return user_info


class PostCreateSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Posts
        fields = ('author', 'title', 'content')

        def create(self, validated_data):
            post = Posts(**validated_data)
            post.save()
            return post