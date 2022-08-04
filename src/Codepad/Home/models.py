from django.db import models
from django_currentuser.middleware import get_current_authenticated_user, get_current_user
from django_currentuser.db.models import CurrentUserField
# Create your models here.

class Code(models.Model):
    user = CurrentUserField()
    SUPPORTED_TYPES = [
        ("py", "Python"),
        ("cpp", "C++"),
        ("java", "Java"),
        ("c", "C"),
        ("js", "Node.JS"),
    ]
    fileextension = models.CharField(choices=SUPPORTED_TYPES, max_length=4)
    code = models.CharField(max_length=1048576)
