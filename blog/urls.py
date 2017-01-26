from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<post_id>[0-9]+)/$', views.indi_post , name='indi_post'),
    url(r'^projects/', views.project_list, name='project_list'),
    url(r'^home/', views.home, name='home1'),
    url(r'^portfolio/', views.portfolio, name='portfolio'),

]