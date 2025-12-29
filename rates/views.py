from rest_framework import viewsets
from .models import RateRequest
from .serializers import RateRequestSerializer


class RateRequestViewSet(viewsets.ModelViewSet):
    queryset = RateRequest.objects.all()
    serializer_class = RateRequestSerializer

    def create(self, request, *args, **kwargs):
        print(f"\n{'=' * 60}")
        print(f"[🔍 VIEWSET] create() method called!")
        print(f"[🔍 VIEWSET] Request method: {request.method}")
        print(f"[🔍 VIEWSET] Request data: {request.data}")
        print(f"[🔍 VIEWSET] Request user: {request.user}")
        print(f"[🔍 VIEWSET] Request auth: {request.auth}")
        print(f"{'=' * 60}\n")

        return super().create(request, *args, **kwargs)