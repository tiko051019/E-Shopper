from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.core.mail import EmailMessage
from .models import *
from .forms import *
from Shopping.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate,login,logout
from django.conf import settings

#--------------------------------------------------------------
#--------------------Login,Register,Logout---------------------
#--------------------------------------------------------------

def login_register_view(request):
    maininfo = MainInfo.objects.get()
    form = CreateUserForm
    log_message, reg_message = "",""

    if request.method == "POST":
        if "register" in request.POST:  
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.email = request.POST.get("email")
                user.save()

                email_msg = EmailMessage(
                    subject=f'Hello {request.POST.get("username")}',
                    body='Sign up completed successfully',
                    from_email=settings.EMAIL_HOST_USER,
                    to=[request.POST.get("email")],
                )
                email_msg.send()
                return redirect("login")
            else:
                reg_message = form.errors

        elif "login" in request.POST:  
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                log_message = "User not found"

    context = {
        "maininfo": maininfo,
        "form": form,
        "log_message": log_message,  # Separate login message
        "reg_message": reg_message,  # Separate register message
    }
    return render(request, "login.html", context)


def Logout(request):
    logout(request)
    return redirect("login")

#--------------------------------------------------------------
#--------------------------------------------------------------
#--------------------------------------------------------------

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self,request):
        maininfo = MainInfo.objects.get()
        carousel = Carousel.objects.all()
        category = Category.objects.all()

        context = {
            'maininfo':maininfo,
            'carousel':carousel,
            'category':category,
        }

        return render(request,self.template_name,context)
    