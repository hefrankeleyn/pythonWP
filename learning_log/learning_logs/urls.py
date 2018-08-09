"""set learning_logs's model """
from django.urls import path,re_path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #main page
    path('',views.index,name='index'),
    #re_path(r'^$',views.index,name='index'),
    re_path(r'^topics/$',views.topics,name='topics'),
    #set special topic
    re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
]
