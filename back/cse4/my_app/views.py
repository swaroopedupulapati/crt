from django.shortcuts import render,redirect

# Create your views here.
from .models import Book
def read_view(request):
    output = Book.objects.all()
    return render(request, "read.html", {"data":output})

from .forms import LoginForm
from django.http import HttpResponse
from django.shortcuts import redirect

def login_view(request):
    if request.method == "POST":
        raw_data = LoginForm(request.POST)
        if raw_data.is_valid():
            e = raw_data.cleaned_data["email"]
            p = raw_data.cleaned_data["password"]
            if e == "swaroopedupulapati1@gmail.com" and p == "swaroop@2004":
                return redirect("read")
            else:
                return HttpResponse("<h1>Invalid Email/Password</h1>")
    else:
        form_fields = LoginForm()
        return render(request, "login.html", {"form": form_fields})