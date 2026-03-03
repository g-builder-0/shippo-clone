from django.db import models


class RateRequest(models.Model):
    carrier = models.CharField(max_length=50)
    service_level = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.carrier} - {self.service_level}: ${self.amount}"


class Address(models.Model):
    """Shipping address for origin or destination"""
    name = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    street1 = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=2, default='US')  # ISO 2-letter
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    is_residential = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"

    class Meta:
        verbose_name_plural = "Addresses"


class Parcel(models.Model):
    """Physical package dimensions and weight"""

    DISTANCE_UNIT_CHOICES = [
        ('in', 'Inches'),
        ('cm', 'Centimeters'),
    ]

    MASS_UNIT_CHOICES = [
        ('lb', 'Pounds'),
        ('oz', 'Ounces'),
        ('kg', 'Kilograms'),
        ('g', 'Grams'),
    ]

    length = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    distance_unit = models.CharField(max_length=2, choices=DISTANCE_UNIT_CHOICES, default='in')

    weight = models.DecimalField(max_digits=10, decimal_places=2)
    mass_unit = models.CharField(max_length=2, choices=MASS_UNIT_CHOICES, default='lb')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.length}x{self.width}x{self.height} {self.distance_unit}, {self.weight} {self.mass_unit}"


class Shipment(models.Model):
    """Complete shipment request linking addresses and parcel"""

    address_from = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='shipments_from'
    )
    address_to = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='shipments_to'
    )
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shipment {self.id}: {self.address_from.city} → {self.address_to.city}"