from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.tweet_list , name = 'tweet_list'),
    path('create/',views.create_tweet , name='create_tweet'),
    path('<int:tweet_id>/edit/',views.edit_tweet,name='edit_tweet'),
    path('<int:tweet_id>/delete/',views.delete_tweet,name='delete_tweet')
    ] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)