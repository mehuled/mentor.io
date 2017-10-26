from django.conf.urls import url
from mentorapp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
]
