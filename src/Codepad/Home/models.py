from django.db import models
from django.contrib.auth.models import User

#Globals
SUPPORTED_TYPES = [
        ("py", "Python"),
        ("cpp", "C++"),
        ("java", "Java"),
        ("c", "C"),
        ("js", "Node.JS"),
    ]

#Model initializers
class CodeManager(models.Manager):
    def create_code(self, user=str(), fileextension=str(), codefile=str()):
        if code not in SUPPORTED_TYPES:
            return
        code = self.create(user, fileextension, codefile)
        return code


# Create your models here.
class Code(models.Model):
    user = models.CharField(max_length=150)
    fileextension = models.CharField(choices=SUPPORTED_TYPES, max_length=4)
    codefile = models.CharField(max_length=1048576)
    objects = CodeManager()


