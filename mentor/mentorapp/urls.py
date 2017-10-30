from django.conf.urls import url
from mentorapp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^register_student/$', views.registerStudent, name='registerStudent'), # NEW MAPPING!
        url(r'^register_mentor/$', views.registerMentor, name='registerMentor'), # NEW MAPPING!

]
