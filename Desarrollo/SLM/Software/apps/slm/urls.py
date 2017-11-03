from django.conf.urls import url

from .views import IndexView, ReservaView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^reserva$', ReservaView.as_view(), name='reserva'),
]
