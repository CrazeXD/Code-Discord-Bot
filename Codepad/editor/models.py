from django.db import models

# Create your models here.
class Code(models.Model):
    title = models.CharField(max_length=30)
    languages = [
        ("cpp", "C++"),
        ("c", "C"),
        ("java", "Java"),
        ("py", "Python")
    ]
    extension = models.CharField(max_length=4, choices=languages, default="cpp")
    code = models.TextField()
    def setDefaultCode(self, codestring: str):
        self.code = models.TextField(default=codestring)
    
        
    
    