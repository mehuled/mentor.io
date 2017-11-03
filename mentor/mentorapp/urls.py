from django.conf.urls import url
from mentorapp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^home/', views.home, name='home'),
        url(r'^about/', views.about, name='about'),
        url(r'^register_student/$', views.registerStudent, name='registerStudent'), # NEW MAPPING!
        url(r'^register_mentor/$', views.registerMentor, name='registerMentor'), # NEW MAPPING!
        url(r'^failed/$', views.failed_login, name='failed_login'), 
        url(r'^login/$', views.welcome, name='welcome'), 
]
