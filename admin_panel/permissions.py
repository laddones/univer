from rest_framework import permissions

from univer.settings import ALLOW_IP_API


class IplistPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        print(ip_addr)
        for i in ALLOW_IP_API:
            for k, v in i.items():
                if v == ip_addr:
                    return True
        return False