from django.conf.urls import url

from .api import SolutionApiView


urlpatterns = [
    url(r'^$', SolutionApiView.as_view(), name='difference'),
]