from django.conf.urls import url
from pricecheck import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.pricecheck, name='pricecheck'),
    url(r'^results$', views.results, name='results'),


]