# pylint: disable=invalid-name
from django.urls import path
from .views import album, views
app_name = "bloge"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),

    path('libraries', album.libraries, name='libraries'),
    path('album/<slug:slug>/', album.album_detail, name='album_detail'),

    path('create/', album.album_create, name='album_create'),
    path('update/<slug:slug>/', album.album_update, name='album_update'),
    path('delete/<slug:slug>/', album.album_delete, name='album_delete'),

    # path('like/<slug:slug>/', album.like_album, name='like_album'),
    path('teachings', views.teachings, name='teachings'),
    path('donations', views.donations, name='donations'),
    path('news', views.news, name='news')
]
