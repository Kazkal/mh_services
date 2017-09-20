from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.list_posts, name='blog'),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
]
