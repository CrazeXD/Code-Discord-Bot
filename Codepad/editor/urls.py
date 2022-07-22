from django.urls import path
from editor import views

urlpatterns = [
    path('', views.load_editor, name="editor")
]