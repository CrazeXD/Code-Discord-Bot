from django.db import models

#Globals
SUPPORTED_TYPES = [
        ("py", "Python"),
        ("cpp", "C++"),
        ("java", "Java"),
        ("c", "C"),
        ("js", "Node.JS"),
    ]

# Create your models here.
class Code(models.Model):
    name = models.CharField(max_length=64, null=True)
    owner = models.CharField(max_length=150, default="")
    fileextension = models.CharField(choices=SUPPORTED_TYPES, max_length=4, verbose_name="Language")
    codefile = models.TextField(max_length=1048576)
    last_edit = models.DateField(auto_now=True)
    def __str__(self):
        return self.name


