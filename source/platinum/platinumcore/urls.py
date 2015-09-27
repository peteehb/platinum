from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from views import index


urlpatterns = patterns(
    '',
    url(r'^$', index, name="index")
)

