from django.urls import path
from . import views

urlpatterns = [
    path("itemform/", views.addproducts, name="addproducts"),
    path("details/<int:id>/", views.details, name="details"), 
    path("edit/<int:id>/", views.edit, name="edit"), 
]
