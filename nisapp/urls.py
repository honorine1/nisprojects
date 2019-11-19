from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^newbiz/',views.new_business,name = 'new_business'),
    url(r'^newpost/',views.new_post,name = 'new_post'),
    url(r'^neighborhood/(?P<neighborhood_id>\d+)',views.neighborhood,name = 'neighborhood'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    # url(r'^update_profile/',views.update_profile,name = 'update_profile'),
    url(r'^search/', views.search_product, name='search_product'),
    # url(r'^search/', views.search_location, name='search_location'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)