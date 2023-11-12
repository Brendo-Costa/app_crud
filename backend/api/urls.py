"""Routes for api app."""
from django.urls import path
from . import views

urlpatterns =[
    path('get/', views.get_blogs, name='get'),
    path('create/', views.post_blog, name='create'),
    path('update/<int:pk>/', views.update_blog, name='update'),
    path('delete/<int:pk>/', views.delete_blog, name='delete'),
]