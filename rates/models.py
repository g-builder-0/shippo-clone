from django.db import models


class RateRequest(models.Model):
    carrier = models.CharField(max_length=50)
    service_level = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.carrier} - {self.service_level}: ${self.amount}"
