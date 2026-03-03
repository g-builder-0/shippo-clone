print(f"[🔍 URLS] rates/urls.py is being loaded!")

from rest_framework.routers import DefaultRouter
from .views import RateRequestViewSet, AddressViewSet, ParcelViewSet, ShipmentViewSet

router = DefaultRouter()
print(f"[🔍 URLS] About to register ViewSets...")

router.register(r'rates', RateRequestViewSet, basename='rate')
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'parcels', ParcelViewSet, basename='parcel')
router.register(r'shipments', ShipmentViewSet, basename='shipment')

print(f"[🔍 URLS] Router URLs generated: {router.urls}")

urlpatterns = router.urls