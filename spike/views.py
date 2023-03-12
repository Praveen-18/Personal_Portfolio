from django.shortcuts import render
from .models import contact
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        print(name , email , comments)
        current_contact = contact(name=name, email=email, comments=comments)
        current_contact.save()
        return render(request, 'spike/index.html')
    return render(request, 'spike/index.html')



