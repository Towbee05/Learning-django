from django import forms
from products.models import Item, Category


class AddProduct(forms.ModelForm):
    # name = forms.CharField(max_length=100000)
    # category = forms.ForeignKey()
    # description = forms.CharField(max_length= 10000000)
    # price = forms.DecimalField(decimal_places = 2, max_digits= 10000)
    # added_to_cart = forms.BooleanField(default=False)
    # in_sales = forms.BooleanField(default=True)
    # image = forms.FileField(blank = False, null=False, upload_to="images/")

    class Meta:
        model = Item
        fields = ("name", "category", "description", "price", "in_sales", "image")

class Editproducts(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "category", "description", "price", "in_sales")