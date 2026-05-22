from .base import BaseCarrier
from decimal import Decimal


class UPSCarrier(BaseCarrier):
    """UPS carrier simulator - middle pricing"""

    carrier_name = "ups"

    BASE_RATES = {
        'ground': Decimal('8.50'),
        'express': Decimal('15.75'),
        'overnight': Decimal('36.00'),
    }

    DELIVERY_DAYS = {
        'ground': 5,
        'express': 2,
        'overnight': 1,
    }