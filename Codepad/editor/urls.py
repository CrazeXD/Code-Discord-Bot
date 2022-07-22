from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_index, name="index"),
    path('<int:pk>/editor', views.load_editor, name="editor"),
    path('<int:pk>/details/', views.project_details, name="details")
]