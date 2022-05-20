from django.urls import path
from blog import views

urlpatterns = [
    path('account/register', views.UserCreate.as_view()),
    path('account/update', views.UserUpdate.as_view()),
]
