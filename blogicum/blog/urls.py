from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
=======
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
>>>>>>> 5b39b732a4e7e651f24306ed54afddc52453896c
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts'),
]
