from django.shortcuts import render

# Create your views here.
def load_editor(request):
    return render(request, 'editor.html', {})