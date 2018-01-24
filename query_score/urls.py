from django.conf.urls import url
from query_score import views

urlpatterns = [
    url('^$', views.Home.as_view(), name='home')
]
