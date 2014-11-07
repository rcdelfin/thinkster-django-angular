from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from authentication.views import LoginView, LogoutView, UserCreateView
from thoughts.views import ThoughtListCreateView, \
    ThoughtRetrieveUpdateDestroyView

urlpatterns = patterns(
    '',

    url(r'^api/v1/users/$', UserCreateView.as_view(), name='user-create'),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url(r'^api/v1/thoughts/$',
        ThoughtListCreateView.as_view(), name='thoughts'),
    url(r'^api/v1/thoughts/(?P<pk>[0-9]+)/$',
        ThoughtRetrieveUpdateDestroyView.as_view(), name='thought'),

    url(r'^.*$',
        TemplateView.as_view(template_name='index.html'), name='index'),
)
