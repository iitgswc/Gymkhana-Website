from django.conf.urls import url
from . import views

app_name = 'editor'

urlpatterns = [

    url(r'^edit/clubs/(?P<club_name>[\w|\W]+)/$', views.editClub.as_view(), name='editClub'),
    url(r'^view/clubs/(?P<club_name>[\w|\W]+)/$', views.viewClub.as_view(), name='viewClub'),

    url(r'^edit/index/$', views.editIndex.as_view(), name='editIndex'),

    url(r'^edit/achievements/$', views.editAchievements.as_view(), name='editAchievements'),

    url(r'^edit/announcements/$', views.editAnnouncements.as_view(), name='editAnnouncements'),

    url(r'^view/index/$', views.viewIndex.as_view(), name='viewIndex'),

    url(r'^view/achievements/$', views.viewAchievements.as_view(), name='viewAchievements'),

    url(r'^view/announcements/$', views.viewAnnouncements.as_view(), name='viewAnnouncements'),

    url(r'^edit/(?P<board_name>[\w|\W]+)/$', views.editBoard.as_view(),name='editBoard'),
    url(r'^view/(?P<board_name>[\w|\W]+)/$', views.viewBoard.as_view(),name='viewBoard'),

    url(r'^Login/$', views.Login.as_view(), name='Login'),

    url(r'^Logout/$', views.Logout, name='Logout'),



]