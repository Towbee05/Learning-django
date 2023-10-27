from django.shortcuts import render,redirect
from .forms import AddProduct,Editproducts
from django.contrib import messages
from .models import Item

# Create your views here.

def addproducts(request):
    form = AddProduct()
    if request.method =="POST":
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Item successfully added")
            form = AddProduct()
            return redirect("/home")

    context = {
        "form" : form
    }
    return render(request, "products/addproducts.html", context)

def details(request, id):
    object_id = Item.objects.get(id = id)
    if request.method == "POST":
        object_id.delete()
        return redirect('home')
    context = {
        "object" : object_id
    }
    return render(request, "products/details.html", context)

def edit(request, id):
    obj = Item.objects.get(id = id)
    form = Editproducts(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = Editproducts(request.FILES)
        return redirect ('home')
    context = {
        "form" : form,
        "id" : obj
    }
    return render(request, "products/edit.html", context) 