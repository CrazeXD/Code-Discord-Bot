from django.db import models

class OwnerField(models.CharField):
    def to_python(self, value):
        return value.lower()
    
