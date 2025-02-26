from rest_framework import routers

from monitoring.publishing import views
from django.urls import re_path

router = routers.SimpleRouter()
router.register(r'cloud', views.CloudSiteViewSet)
router.register(r'grid', views.GridSiteViewSet)
router.register(r'gridsync', views.GridSiteSyncViewSet)

urlpatterns = [
    re_path(
        r'^cloud/(?P<SiteName>[a-zA-Z0-9.-]+)/$',
        views.CloudSiteViewSet.as_view({'get': 'retrieve'}),
        name='cloudsite-detail'
    ),
    re_path(
        r'^grid/(?P<SiteName>[a-zA-Z0-9.-]+)/$',
        views.GridSiteViewSet.as_view({'get': 'retrieve'}),
        name='gridsite-detail'
    ),
    re_path(
        r'^gridsync/(?P<SiteName>[a-zA-Z0-9.-]+)/$',
        views.GridSiteSyncViewSet.as_view({'get': 'retrieve'}),
        name='gridsitesync-detail'
    ),
    re_path(
        r'^gridsync/(?P<SiteName>[a-zA-Z0-9.-]+)/(?P<YearMonth>[0-9-]+)/$',
        views.GridSiteSyncSubmitHViewSet.as_view({'get': 'retrieve'}),
        name='gridsync_submithost'
    ),
]

urlpatterns += router.urls
