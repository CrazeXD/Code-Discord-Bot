from django.shortcuts import render
from editor.models import Code
# Create your views here.
def load_index(request):
    return render(request, 'index.html', {})
def project_details(request, pk):
    codes = Code.objects.get(pk)
    context = {
        'codes': codes
    }
    return render(request, 'projectdetails.html', context)
def load_editor(request, pk):
    code = Code.objects.get(pk=pk)
    context = {
        'codes': code
    }
    return render(request, 'editor.html', context)