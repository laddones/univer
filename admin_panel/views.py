from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from admin_panel.models.client import Client, Links, LinkClientStatus
from admin_panel.permissions import IplistPermission
from admin_panel.serializers import ClientSerializer, LinksSerializer, GetLinkClientSerializer, LinkByUserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IplistPermission,)


class LinksViewSet(viewsets.ModelViewSet):
    serializer_class = LinksSerializer
    queryset = Links.objects.all()
    permission_classes = (IplistPermission, )


class GetLinkByUser(APIView):

    def get(self, request, **kwargs):
        client_id = kwargs.get('client_id', None)
        client = Client.objects.all().filter(pk=client_id).first()
        if client:
            link = Links.objects.all().filter(link_status=Links.LinkStatusChoices.PUBLISHED)\
                .exclude(client_link__client=client.pk)[:1]
            print(link)
            if link:
                return Response(GetLinkClientSerializer(link[0]).data)
            else:
                return Response({'link': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'client': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)


class LinkByUserViewSet(viewsets.ModelViewSet):
    serializer_class = LinkByUserSerializer
    queryset = LinkClientStatus.objects.all()
    permission_classes = (IplistPermission, )


