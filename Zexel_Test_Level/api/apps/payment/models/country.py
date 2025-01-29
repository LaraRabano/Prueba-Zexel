import uuid
from django.db import models

class Country(models.Model):
   
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.code} {self.description}"

"""No conozco la aplicación y no se me ocurre qué otras características podría tener este modelo, pero en una aplicación real, no sería descabellado
pensar en tener campos que recojan los impuestos que se tendrían que aplicar a esos pagos o algo similar."""