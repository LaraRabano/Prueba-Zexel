import re
import uuid
from django.db import models
from django.db.models import Q, CheckConstraint


class PaymentUser(models.Model):
   
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    dni = models.CharField(max_length=9, unique=True, null=False) 
    adress = models.CharField(max_length=250)
    billing_adress = models.CharField(max_length=250, unique=True, null=False)
    bank_account = models.CharField(max_length=34, unique=True)
    email = models.EmailField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models(auto_now=True)

    def __str__(self):
        return f"{self.id}{self.name}{self.surname}{self.email}{self.dni}"

    class Meta:
        constraints = [
            #Validación del DNI. Habría que darle una vuelta para hacerlo más internacional.
            CheckConstraint(
                check = Q(dni__regex = r'^\d{8}[A-Z]¢'),
                name = 'check_dni_format'
            ),
            #Validación del IBAN.
            CheckConstraint(
                check = Q(bank_account__regex = r'^[A-Z]{2}\d{2}\[A-Z0-9]{11,30}¢'),
                name = 'check_bank_account'
            )
        ]
    
    
