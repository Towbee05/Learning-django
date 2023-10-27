from django.shortcuts import render
from products.models import Item
from django.core.mail import send_mail
from products.views import details

# Create your views here.
def home(request):
    obj = Item.objects.all()
    context = {
        "objects" : obj
    }

    if request.method == "POST": 
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject=f"{firstname} {lastname}",
            message = message,
            from_email=email,
            recipient_list=[],
            fail_silently=False
        )
    return render(request, "core/home.html", context)
