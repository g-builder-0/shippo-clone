from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import RateRequest, Address, Parcel, Shipment, Rate
from .serializers import RateRequestSerializer, AddressSerializer, ParcelSerializer, ShipmentSerializer, RateSerializer
from .carriers.fedex import FedExCarrier
from .carriers.ups import UPSCarrier
from .carriers.usps import USPSCarrier

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

    @action(detail=True, methods=['post'])
    def get_rates(self, request, pk=None):
        """
        Get shipping rates from all carriers for this shipment

        POST /api/shipments/{id}/get_rates/
        """
        shipment = self.get_object()

        # Initialize carriers
        carriers = [
            FedExCarrier(),
            UPSCarrier(),
            USPSCarrier(),
        ]

        service_levels = ['ground', 'express', 'overnight']

        # Collect all rates
        rates = []
        for carrier in carriers:
            for service_level in service_levels:
                # Calculate rate
                rate_data = carrier.calculate_rate(shipment, service_level)

                # Create Rate object
                rate = Rate.objects.create(
                    shipment=shipment,
                    carrier=carrier.carrier_name,
                    service_level=service_level,
                    amount_carrier=rate_data['amount_carrier'],
                    amount_charged=rate_data['amount_charged'],
                    estimated_days=rate_data['estimated_days']
                )
                rates.append(rate)

        # Serialize and return
        serializer = RateSerializer(rates, many=True)
        return Response(serializer.data)
