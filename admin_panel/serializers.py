from rest_framework import serializers, viewsets

from .models.client import Client, Links, LinkClientStatus
from .permissions import IplistPermission


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['time_create', 'time_update']


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'
        read_only_fields = ['time_create', 'time_update']


class GetLinkClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['id', 'link', 'link_type', 'link_status', 'description']


class LinkByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkClientStatus
        fields = '__all__'
        read_only_fields = ['time_create', 'time_update']
