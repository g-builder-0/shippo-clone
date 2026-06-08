from decimal import Decimal
import random


class BaseCarrier:
    """Base class for all carrier simulators"""

    carrier_name = "Base"

    # Base rates per service level (USD)
    BASE_RATES = {
        'ground': Decimal('8.00'),
        'express': Decimal('15.00'),
        'overnight': Decimal('35.00'),
    }

    # Estimated delivery days
    DELIVERY_DAYS = {
        'ground': 5,
        'express': 2,
        'overnight': 1,
    }

    def calculate_rate(self, shipment, service_level):
        """
        Calculate shipping rate based on shipment details

        Args:
            shipment: Shipment model instance
            service_level: 'ground', 'express', or 'overnight'

        Returns:
            dict with 'amount' and 'estimated_days'
        """
        # Start with base rate
        rate = self.BASE_RATES[service_level]

        # Add weight surcharge ($0.50 per pound over 5 lbs)
        weight = float(shipment.parcel.weight)
        if weight > 5:
            rate += Decimal(str((weight - 5) * 0.50))

        # Add distance surcharge (simplified - $0.10 per 100 miles)
        distance = self._calculate_distance(shipment.address_from, shipment.address_to)
        distance_surcharge = Decimal(str(distance / 100 * 0.10))
        rate += distance_surcharge

        # Add random variation (simulate real API fluctuation)
        variation = Decimal(str(random.uniform(-0.50, 0.50)))
        rate += variation

        # Round to 2 decimal places
        rate = rate.quantize(Decimal('0.01'))

        MARGINS = {
            'ground': Decimal('0.08'),
            'express': Decimal('0.15'),
            'overnight': Decimal('0.15'),
        }

        margin = MARGINS[service_level]
        amount_charged = (rate * (1 + margin)).quantize(Decimal('0.01'))

        return {
            'amount_carrier': rate,
            'amount_charged': amount_charged,
            'estimated_days': self.DELIVERY_DAYS[service_level]
        }

    def _calculate_distance(self, address_from, address_to):
        """
        Simplified distance calculation
        In real life, would use geocoding API

        For now: same city = 10 miles, same state = 200 miles, different state = 1000 miles
        """
        if address_from.city == address_to.city:
            return 10
        elif address_from.state == address_to.state:
            return 200
        else:
            return 1000