from . import views
from django.urls import path

urlpatterns = [
    path('add_blogs', views.add_blogs, name='add_blogs'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]