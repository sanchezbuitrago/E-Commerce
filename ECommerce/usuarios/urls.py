from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^usuario/',views.createuserlinkedin, name="createuserlinkedin"),
    url(r'^login/',views.auth_login, name='authentication'),
    url(r'^logout/',auth_views.logout, {'next_page':'/'},name='logout')
]
