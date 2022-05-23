from django.urls import path
from blog import views

urlpatterns = [
    path('account/register', views.UserCreate.as_view()),
    path('account/update', views.UserUpdate.as_view()),
    path('account/set/additional', views.CreateAndUpdateUsersAdditionalInfo.as_view()),
    path('post/detail/<int:pk>/', views.DetailEditRemovePostAPI.as_view()),
    path('posts/create', views.PostCreate.as_view(), name='post_create_api'),
    path('posts/list', views.PostList.as_view())

]
