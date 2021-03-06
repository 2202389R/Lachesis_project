from django.conf.urls import url
from lachesis import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^add_genre/$', views.add_genre, name='add_genre'),
    url(r'^genre/(?P<genre_name_slug>[\w\-]+)/$',
        views.show_genre, name='show_genre'),
    url(r'^genre/(?P<genre_name_slug>[\w\-]+)/add_story/$',
        views.add_story, name='add_story'),
    url(r'^story/(?P<story_name_slug>[\w\-]+)/add_segment/$',
        views.add_segment, name='add_segment'),
    url(r'^story/(?P<story_name_slug>[\w\-]+)/$',
        views.show_story, name='show_story'),
    url(r'^segment/(?P<segment_name_slug>[\w\-]+)/$',
        views.show_segment, name='show_segment'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile')
]
