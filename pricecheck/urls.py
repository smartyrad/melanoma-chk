from django.conf.urls import url
from pricecheck import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.pricecheck, name='pricecheck'),
    url(r'^results$', views.results, name='results'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
