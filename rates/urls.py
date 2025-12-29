print(f"[🔍 URLS] rates/urls.py is being loaded!")

from rest_framework.routers import DefaultRouter
from .views import RateRequestViewSet

router = DefaultRouter()
print(f"[🔍 URLS] About to register RateRequestViewSet...")
router.register(r'rates', RateRequestViewSet, basename='rate')
print(f"[🔍 URLS] Router URLs generated: {router.urls}")

urlpatterns = router.urls