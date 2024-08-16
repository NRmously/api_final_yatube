from django.urls import path, include
from rest_framework import routers

from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(
    'groups',
    GroupViewSet,
    basename='groups',
)
router.register(
    'posts',
    PostViewSet,
    basename='posts',
)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router.register(
    'follow',
    FollowViewSet,
    basename='follow',
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
