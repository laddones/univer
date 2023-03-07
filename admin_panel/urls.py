from django.urls import path, include
from rest_framework import routers

from admin_panel.views import ClientViewSet, LinksViewSet, GetLinkByUser, LinkByUserViewSet

router = routers.DefaultRouter()

router.register(r'client', ClientViewSet)
router.register(r'links', LinksViewSet)
router.register(r'links_client', LinkByUserViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/get_link/<int:client_id>/', GetLinkByUser.as_view())
]
