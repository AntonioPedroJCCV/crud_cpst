from django.urls import include, path
from rest_framework import routers
from crud.views import CustomerViewSet, ProductViewSet, SportViewSet, TeamViewSet

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'product', ProductViewSet)
router.register(r'sport', SportViewSet)
router.register(r'team', TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]