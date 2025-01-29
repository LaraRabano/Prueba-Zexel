import uuid
from django.db import models

class CurrencyTypes(models.Model):
   
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.code} {self.description}"
