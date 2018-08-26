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
    # add new_topic page
    re_path(r'^new_topic/$',views.new_topic,name='new_topic'),
    # use to add new entry
    re_path(r'^new_entry/(?P<topic_id>\d+)$',views.new_entry,name='new_entry'),
    # edit snip
    re_path(r'^edit_entry/(?P<entry_id>\d+)$',views.edit_entry,
            name='edit_entry')
]
