from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^rsvp_search/', views.search_result, name="search"),
	url(r'^(?P<rsvp_id>[0-9]+)/$', views.rsvp_respond, name="respond"),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name="results")
]