from django.conf.urls import url
from mentorapp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^register_student/$', views.registerStudent, name='registerStudent'), # NEW MAPPING!
        url(r'^register_mentor/$', views.registerMentor, name='registerMentor'), # NEW MAPPING!
        url(r'^failed/$', views.failed_login, name='failed_login'),
        url(r'^home/$', views.home, name='home'),# create this one
        url(r'^search/$', views.search, name='search'), # create this one
        url(r'^apply/$', views.apply, name='apply'),  #create this one
        url(r'^home/$', views.welcome, name='welcome'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^search/$', views.search, name='search'),
        url(r'^profile/$', views.profile, name='profile'),
        url(r'^mysession/$', views.mysession, name='mysession'),
        url(r'^course/$', views.course, name='course'),
]
