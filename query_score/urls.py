from django.conf.urls import url
from query_score import views

urlpatterns = [
    url('^$', views.Home.as_view(), name='home'),
    url(r'query_by_keyword/$', views.QueryView.as_view(), name='query_by_keyword'),
]
