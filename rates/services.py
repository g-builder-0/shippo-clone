import uuid
import os
from decimal import Decimal
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from django.conf import settings


class LabelGenerator:
    """
    Generates a mock shipping label PDF.
    In production this would call the carrier API to get a real label.
    """

    def generate_tracking_number(self, carrier):
        """Generate a fake tracking number per carrier format"""
        unique = uuid.uuid4().hex[:16].upper()

        if carrier == 'usps':
            return f"9400{unique}"
        elif carrier == 'ups':
            return f"1Z{unique}"
        elif carrier == 'fedex':
            return f"7489{unique}"
        else:
            return f"TRK{unique}"

    def generate_label(self, transaction):
        """
        Generate a PDF label and save it to media/labels/.
        Returns the file path relative to MEDIA_ROOT.
        """
        rate = transaction.rate
        shipment = rate.shipment
        address_from = shipment.address_from
        address_to = shipment.address_to

        # Ensure labels directory exists
        labels_dir = os.path.join(settings.MEDIA_ROOT, 'labels')
        os.makedirs(labels_dir, exist_ok=True)

        filename = f"label_{transaction.id}_{transaction.tracking_number}.pdf"
        filepath = os.path.join(labels_dir, filename)

        # Generate PDF
        c = canvas.Canvas(filepath, pagesize=(4 * inch, 6 * inch))

        # Carrier and service
        c.setFont("Helvetica-Bold", 14)
        c.drawString(0.25 * inch, 5.5 * inch, f"{rate.carrier.upper()} {rate.service_level.upper()}")

        # Tracking number
        c.setFont("Helvetica", 10)
        c.drawString(0.25 * inch, 5.1 * inch, f"Tracking: {transaction.tracking_number}")

        # From address
        c.setFont("Helvetica-Bold", 9)
        c.drawString(0.25 * inch, 4.6 * inch, "FROM:")
        c.setFont("Helvetica", 9)
        c.drawString(0.25 * inch, 4.4 * inch, address_from.name)
        c.drawString(0.25 * inch, 4.25 * inch, address_from.street1)
        c.drawString(0.25 * inch, 4.1 * inch, f"{address_from.city}, {address_from.state} {address_from.zip_code}")

        # To address
        c.setFont("Helvetica-Bold", 12)
        c.drawString(0.25 * inch, 3.5 * inch, "TO:")
        c.setFont("Helvetica", 12)
        c.drawString(0.25 * inch, 3.2 * inch, address_to.name)
        c.drawString(0.25 * inch, 2.95 * inch, address_to.street1)
        c.drawString(0.25 * inch, 2.7 * inch, f"{address_to.city}, {address_to.state} {address_to.zip_code}")

        # Amount
        c.setFont("Helvetica", 9)
        c.drawString(0.25 * inch, 0.5 * inch, f"Amount charged: ${transaction.amount}")

        c.save()

        return f"labels/{filename}"