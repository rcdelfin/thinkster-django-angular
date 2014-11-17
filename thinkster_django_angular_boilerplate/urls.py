from django.conf.urls import include, patterns, url
from django.views.generic.base import TemplateView

from rest_framework.routers import DefaultRouter

from authentication.views import AccountViewSet, LoginView, LogoutView
from posts.views import PostViewSet

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = patterns(
    '',

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url(r'^.*$',
        TemplateView.as_view(template_name='index.html'), name='index'),
)
