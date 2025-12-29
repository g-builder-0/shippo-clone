from rest_framework import serializers
from .models import RateRequest


class RateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateRequest
        fields = ['id', 'carrier', 'service_level', 'amount', 'created_at']

    def validate(self, data):
        print(f"[🔍 SERIALIZER] validate() called with: {data}")
        print(f"[🔍 SERIALIZER] Type of data: {type(data)}")
        return data