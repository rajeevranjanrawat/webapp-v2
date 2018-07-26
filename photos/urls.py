from django.conf.urls import url
from photos import views


urlpatterns = [

    url(r'^photo$', views.photo_list, name='gallery'),

]