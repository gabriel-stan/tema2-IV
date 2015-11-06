from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /votos/
    url(r'^$', views.index, name='index'),
    # ex: /votos/5/results/
    url(r'^(?P<empresa_id>[0-9]+)/$', views.results, name='results'),
]