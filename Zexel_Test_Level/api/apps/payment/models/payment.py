import uuid
from django.db import models

from Zexel_Test_Level.api.apps.payment.models.concept import ConceptTypes
from Zexel_Test_Level.api.apps.payment.models.country import Country
from Zexel_Test_Level.api.apps.payment.models.currency_types import CurrencyTypes
from Zexel_Test_Level.api.apps.payment.models.status_choice import StatusChoice
from Zexel_Test_Level.api.apps.payment.models.user import PaymentUser

class Payment(models.Model):
    """STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Requested', 'Requested'),
        ('Approved', 'Approved'),
        ('Paid', 'Paid'),
        ('Deleted', 'Deleted'),
    ]"""
    
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    source_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    source_currency = models.ForeignKey(CurrencyTypes, on_delete=models.CASCADE)
    source_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    target_currency = models.ForeignKey(CurrencyTypes, on_delete=models.CASCADE)
    target_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(StatusChoice, on_delete=models.CASCADE)
    concept = models.ForeignKey(ConceptTypes, on_delete=models.CASCADE)
    rate_exchange = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    sender_id = models.ForeignKey(PaymentUser, on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(PaymentUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.source_amount} {self.source_currency} to {self.target_amount} {self.target_currency}"
