from django.db import models
from django.contrib.auth.models import User
from .fields import OwnerField
#Globals
SUPPORTED_TYPES = [
        ("py", "Python"),
        ("cpp", "C++"),
        ("java", "Java"),
        ("c", "C"),
        ("js", "Node.JS"),
    ]
DEFAULT_FOR_LANG = {
    "py": "print(\"Hello world!\")",
    "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n\tcout << \"Hello world!\" << endl;\n}",
    "java": "class Main {\n\tpublic static void Main(String[] args) {\n\t\tSystem.out.println(\"Hello world!\");\n\t}]n}",
    "c": '''#include <stdio.h>
            int main() {
            \tprintf("Hello, World!");
            return 0;
            }
        ''',
    "js": "console.log('Hello World');"        
}
# Create your models here.
class Code(models.Model):
    name = models.CharField(max_length=64, null=True, pk=True)
    owner = OwnerField(max_length=150, default="")
    fileextension = models.CharField(choices=SUPPORTED_TYPES, max_length=4, verbose_name="Language")
    codefile = models.TextField(max_length=1048576)
    last_edit = models.DateField(auto_now=True)
    def __str__(self):
        return self.name


