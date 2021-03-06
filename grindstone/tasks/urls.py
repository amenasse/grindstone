from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.TaskList.as_view(), name='list'),
    url(r'^new/$', views.TaskCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.TaskDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.TaskUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.TaskDelete.as_view(), name='delete'),
]
