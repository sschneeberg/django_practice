from django.urls import path
from . import views

urlpatterns = {
    path('', views.index, name='index'),
    path('user/<str:username>', views.profile, name='profile'),
    path('user/<str:username>/add', views.GithubCreate.as_view(), name='github_create'),
    path('user/<int:pk>/delete', views.GithubDelete.as_view(), name='github_delete'),
}