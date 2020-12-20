from django.conf.urls import include, url
from register import views


urlpatterns = [
    url(r'^consent/',views.consent)
]
