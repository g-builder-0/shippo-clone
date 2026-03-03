from rest_framework import viewsets
from .models import RateRequest, Address, Parcel, Shipment
from .serializers import RateRequestSerializer, AddressSerializer, ParcelSerializer, ShipmentSerializer


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


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
