from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /votos/
    url(r'^$', views.index, name='index'),
]