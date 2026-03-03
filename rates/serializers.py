from rest_framework import serializers
from .models import RateRequest, Address, Parcel, Shipment


class RateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateRequest
        fields = ['id', 'carrier', 'service_level', 'amount', 'created_at']

    def validate(self, data):
        print(f"[🔍 SERIALIZER] validate() called with: {data}")
        print(f"[🔍 SERIALIZER] Type of data: {type(data)}")
        return data


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id', 'name', 'company', 'street1', 'street2',
            'city', 'state', 'zip_code', 'country',
            'phone', 'email', 'is_residential', 'created_at'
        ]


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = [
            'id', 'length', 'width', 'height', 'distance_unit',
            'weight', 'mass_unit', 'created_at'
        ]


class ShipmentSerializer(serializers.ModelSerializer):
    # Nested serializers for detailed responses (read)
    address_from = AddressSerializer(read_only=True)
    address_to = AddressSerializer(read_only=True)
    parcel = ParcelSerializer(read_only=True)

    # IDs for creating shipments (write)
    address_from_id = serializers.IntegerField(write_only=True)
    address_to_id = serializers.IntegerField(write_only=True)
    parcel_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Shipment
        fields = [
            'id', 'address_from', 'address_to', 'parcel',
            'address_from_id', 'address_to_id', 'parcel_id',
            'created_at', 'updated_at'
        ]