from django.shortcuts import render
from mysite.models import Contacts
# Create your views here.


def Index(request):
    return render(request, "mysite/index.html")


def Home(request):
    return render(request, "mysite/home.html")


def Contact(request):
    if request.method == 'POST':
        frm_email =request.POST.get("email")
        frm_subject =request.POST.get("subject")
        frm_comments =request.POST.get("comments")
        cont = Contacts(email=frm_email,subject=frm_subject,comments=frm_comments)
        cont.save()

        replay ={'message':"Successfully submit"}        
        return render(request, "mysite/contact.html",replay)
    else:
        return render(request, "mysite/contact.html")


def Portfolio(request):
    return render(request, "mysite/portfolio.html")
