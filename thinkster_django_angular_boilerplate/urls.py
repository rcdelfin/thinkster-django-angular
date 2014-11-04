from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from authentication.views import UserCreateView

urlpatterns = patterns(
    '',

    url('^api/v1/users/$', UserCreateView.as_view(), name='user-create'),

    url('^.*$', TemplateView.as_view(template_name='index.html'), name='index'),
)
