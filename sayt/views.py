from django.shortcuts import render

from sayt.models import Contact


# Create your views here.


def index(requests):
    ctx = {}
    if requests.POST:
        message = requests.POST.get('message')
        subject = requests.POST.get('subject')
        email = requests.POST.get('email')
        Contact.objects.create(
             message=message, subject=subject, email=email
        )

        ctx = {
            "contact": index,

        }
    return render(requests, "index.html", ctx)