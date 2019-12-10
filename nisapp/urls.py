from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^signUp/$',views.signUp,name='signUp'),
    url(r'^logIn/$',views.logIn,name='logIn'),
    url(r'^logOut/$',views.logOut,name='logOut'),
    url('^$',views.welcome,name = 'welcome'),
    url(r'^index/',views.index,name = 'index'),
    url(r'^newbiz/',views.new_business,name = 'new_business'),
    url(r'^newpost/',views.new_post,name = 'new_post'),
    url(r'^neighborhood/(?P<neighborhood_id>\d+)',views.neighborhood,name = 'neighborhood'),
    # url(r'^new/addprofile$', views.addprofile, name='addprofile'),
     url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^update_profile/',views.update_profile,name = 'update_profile'),

    url(r'^viewProduct/', views.viewProduct, name='viewProduct'),
    url(r'^search/', views.search_product, name='search_product'),
    url(r'^search/', views.search_location, name='search_location'),
     url(r'^search_neighborhood/', views.search_neighborhood, name='search_neighborhood'),
    url(r'^viewBusiness/', views.viewBusiness, name='viewBusiness'),
    url(r'^viewBusinessDetails/(\d+)', views.viewBusinessDetails, name='viewBusinessDetails'),
    url(r'^join/(?P<neighborhood_id>\d+)',views.joinFunc,name = 'join'),   
 
    
    
    # url(r'', views.default_map, name="default"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)