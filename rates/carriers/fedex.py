from .base import BaseCarrier
from decimal import Decimal


class FedExCarrier(BaseCarrier):
    """FedEx carrier simulator - slightly more expensive but faster"""

    carrier_name = "fedex"

    BASE_RATES = {
        'ground': Decimal('9.00'),  # $1 more than base
        'express': Decimal('16.50'),
        'overnight': Decimal('38.00'),
    }

    DELIVERY_DAYS = {
        'ground': 4,  # 1 day faster
        'express': 2,
        'overnight': 1,
    }