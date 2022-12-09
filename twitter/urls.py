from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('likes/<int:post_id>/', views.likes, name='likes')
]