from rest_framework import serializers

from monitoring.publishing.models import (
    CloudSite,
    GridSite,
    GridSiteSync,
    GridSiteSyncSubmitH
)


class GridSiteSerializer(serializers.HyperlinkedModelSerializer):
    # Override default format with None so that Python datetime is used as
    # ouput format. Encoding will be determined by the renderer and can be
    # formatted by a template filter.
    updated = serializers.DateTimeField(format=None)

    class Meta:
        model = GridSite
        fields = (
            'url',
            'SiteName',
            'updated'
        )

        # Sitename substitutes pk
        lookup_field = 'SiteName'
        extra_kwargs = {
            'url': {'view_name': 'gridsite-detail','lookup_field': 'SiteName'}
        }

class GridSiteSyncSerializer(serializers.HyperlinkedModelSerializer):
    # Override default format with None so that Python datetime is used as
    # ouput format. Encoding will be determined by the renderer and can be
    # formatted by a template filter.

    class Meta:
        model = GridSiteSync
        fields = (
            'url',
            'SiteName',
            'YearMonth',
            'RecordStart',
            'RecordEnd',
            'RecordCountPublished',
            'RecordCountInDb',
            'SyncStatus'
        )

        # Sitename substitutes pk
        lookup_field = 'SiteName'
        extra_kwargs = {
            'url': {'lookup_field': 'SiteName'}
        }


class CloudSiteSerializer(serializers.HyperlinkedModelSerializer):
    # Override default format with None so that Python datetime is used as
    # ouput format. Encoding will be determined by the renderer and can be
    # formatted by a template filter.
    updated = serializers.DateTimeField(format=None)

    class Meta:
        model = CloudSite
        fields = (
            'url',
            'SiteName',
            'Vms',
            'Script',
            'updated'
        )

        # Sitename substitutes pk
        lookup_field = 'SiteName'
        extra_kwargs = {
            'url': {'view_name': 'cloudsite-detail', 'lookup_field': 'SiteName'}
        }

class GridSiteSyncSubmitHSerializer(serializers.HyperlinkedModelSerializer):
    # Override default format with None so that Python datetime is used as
    # ouput format. Encoding will be determined by the renderer and can be
    # formatted by a template filter.

    class Meta:
        model = GridSiteSyncSubmitH
        fields = (
            'url',
            'SiteName',
            'YearMonth',
            'RecordStart',
            'RecordEnd',
            'RecordCountPublished',
            'RecordCountInDb',
            'SubmitHost'
        )

        lookup_fields = ('SiteName', 'YearMonth')
