from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.core.mail import EmailMessage
from .models import *
from .forms import *
from Shopping.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.http import HttpResponse

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
                    from_email=EMAIL_HOST_USER,
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

def MainInfoF(context):
    context['maininfo'] = MainInfo.objects.get()
    context['gallery'] = Gallery.objects.all() 

def MainInlcude(context):
    dct = {}
    for i in Items.objects.all():
        dct[i.brand] = Items.objects.filter(brand = i.brand).count()
    context['category'] = Category.objects.all()
    context['dct'] = dct




class HomeListView(ListView):
    template_name = 'index.html'

    def get(self,request):
        carousel = Carousel.objects.all()
        category = Category.objects.all()
        items = Items.objects.all()[:6]
        itemsname = ItemsName.objects.all()
        
        context = {
            'carousel':carousel,
            'category':category,
            'items':items,
            'itemsname':itemsname,

        }

        MainInfoF(context)
        MainInlcude(context)


        return render(request,self.template_name,context)
    
class ProductsPage(ListView):
    template_name = 'shop.html'

    def get(self,request):
        products = Products.objects.get()
        allitems = Items.objects.all()

        context = {
            'products':products,
            'allitems':allitems,
        }
        MainInfoF(context)
        MainInlcude(context)

        return render(request,self.template_name,context)
    

class ContactPage(DetailView):
    template_name = 'contact-us.html'
    
    def get(self,request):
        if request.user.is_authenticated:
            name = request.user.username
            email = request.user.email
        else:
            name = ''
            email = ''

        form = MessageForm()

        context = {
            'name':name,
            'email':email,
            'form':form,
        }

        MainInfoF(context)

        return render(request,self.template_name,context) 

    def post(self,request):
        form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            email = EmailMessage(
                subject=f'Administrative unswer to {request.POST.get('username')}',
                body = 'We will unswer you soon',
                from_email=EMAIL_HOST_USER,
                to=[request.POST.get('email')]
            )
            email.send()
            return redirect('contact')
        
        context = {
            'form':form
        }
        MainInfoF(context)
        return render(request,self.template_name,context)
    


def filter_products(request, category_name, subcategory_name=''):
    category = Category.objects.filter(name=category_name).first()
    if not category:
        return HttpResponse("Category not found")
    if subcategory_name:
        subcategory = SubCategory.objects.filter(subname=subcategory_name, key=category).first()
        if subcategory:
            items = Items.objects.filter(key1=category, key2=subcategory)
        else:
            return HttpResponse("Subcategory not found")
    else:
        items = Items.objects.filter(key1=category)
    carousel = Carousel.objects.all()
    category = Category.objects.all()
    itemsname = ItemsName.objects.all()
    
    context = {
        'carousel':carousel,
        'category':category,
        'items':items,
        'itemsname':itemsname,
        'items': items,
        'categories': Category.objects.all()
    }
    MainInfoF(context)
    MainInlcude(context)
    return render(request, 'index.html', context)


