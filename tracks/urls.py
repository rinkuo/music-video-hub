from django.urls import path
from . import views

app_name = 'tracks'

urlpatterns = [
    path('', views.index, name='index'),
    path('music-list/', views.track_list, name='music_list'),
    path('music/<int:pk>/', views.track_detail, name='music_detail'),
    path('music/create/', views.track_create, name='music_create'),
    path('music/<int:pk>/update/', views.track_update, name='music_update'),
    path('music/<int:pk>/delete/', views.track_delete, name='music_delete_confirm'),
]
