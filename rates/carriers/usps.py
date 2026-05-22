from .base import BaseCarrier
from decimal import Decimal


class USPSCarrier(BaseCarrier):
    """USPS carrier simulator - cheapest but slowest"""

    carrier_name = "usps"

    BASE_RATES = {
        'ground': Decimal('7.00'),  # Cheapest
        'express': Decimal('13.50'),
        'overnight': Decimal('32.00'),
    }

    DELIVERY_DAYS = {
        'ground': 7,  # Slowest
        'express': 3,
        'overnight': 1,
    }