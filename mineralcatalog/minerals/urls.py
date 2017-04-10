from django.conf.urls import url

from . import views

urlpatterns = [

   url(r'^$', views.minerals, name='mineral_list'),
   url(r'random/', views.random_mineral, name='random_mineral'),
   url(r'(?P<pk>\d+)/$',views.mineral_detail, name='mineral_detail'),
   
]