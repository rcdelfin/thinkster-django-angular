from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from authentication.views import LoginView, LogoutView, UserCreateView, \
    UserDestroyView, UserProfileRetrieveUpdateView
from posts.views import PostListCreateView, \
    PostRetrieveUpdateDestroyView, UserPostsListView

urlpatterns = patterns(
    '',

    url(r'^api/v1/users/$', UserCreateView.as_view(), name='user-create'),
    url(r'^api/v1/users/(?P<pk>[0-9]+)/$',
        UserDestroyView.as_view(), name='user-destroy'),
    url(r'^api/v1/users/(?P<user__username>[a-zA-Z0-9_@+-]+)/$',
        UserProfileRetrieveUpdateView.as_view(), name='profile'),
    url(r'^api/v1/users/(?P<user__username>[a-zA-Z0-9_@+-]+)/posts/$',
        UserPostsListView.as_view(), name='profile-posts'),

    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url(r'^api/v1/posts/$', PostListCreateView.as_view(), name='posts'),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)/$',
        PostRetrieveUpdateDestroyView.as_view(), name='post'),

    url(r'^.*$',
        TemplateView.as_view(template_name='index.html'), name='index'),
)
