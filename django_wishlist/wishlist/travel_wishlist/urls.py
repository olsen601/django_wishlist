from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.place_list, name='place_list'),
    url(r'^visited$', views.places_visited, name='places_visited'),
    url(r'^isvisited$', views.place_is_visited, name='place_is_visited'),
    url(r'^place/(?P<pk>\d+)$', views.place, name='place'),
]

# links the url to the proper view function using regular expressions,
# originally url(r'^place/(?:place-(?P<pk>\d+)/)?$', views.place, name='place')
# but /place/place-3/ was redundant
