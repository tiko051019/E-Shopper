from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView,DetailView
from django.utils.encoding import force_bytes
from Shopping.settings import EMAIL_HOST_USER
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
from .models import *
from .forms import *
import random
import math

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
        "log_message": log_message,  
        "reg_message": reg_message, 
    }
    return render(request, "login.html", context)


def Logout(request):
    logout(request)
    return redirect("login")

#--------------------------------------------------------------
#--------------------------Functions---------------------------
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


#--------------------------------------------------------------
#---------------------------Home-------------------------------
#--------------------------------------------------------------

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
        SaveItems_Id_F(request,context)
        MainInfoF(context)
        MainInlcude(context)


        return render(request,self.template_name,context)
    
def filter_home_products(request, category_name, subcategory_name=''):
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
        'categories': Category.objects.all()
    }
    MainInfoF(context)
    MainInlcude(context)
    SaveItems_Id_F(request,context)
    return render(request, 'index.html', context)
    
#--------------------------------------------------------------
#------------------------Products------------------------------
#--------------------------------------------------------------

class ProductsPage(ListView):
    template_name = 'shop.html'

    def get(self,request):
        products = Products.objects.get()
        allitems = Items.objects.all()
        paginator = Paginator(allitems, 9) 
        page_number = request.GET.get('page') 
        page_obj = paginator.get_page(page_number)
            
        context = {
            'products':products,
            'page_obj':page_obj,
            'allitems':allitems,
        }
        MainInfoF(context)
        MainInlcude(context)
        SaveItems_Id_F(request,context)

        return render(request,self.template_name,context)

def filter_products(request, category_name, subcategory_name=''):
    category = Category.objects.filter(name=category_name).first()
    if not category:
        return HttpResponse("Category not found")
    if subcategory_name:
        subcategory = SubCategory.objects.filter(subname=subcategory_name, key=category).first()
        if subcategory:
            allitems = Items.objects.filter(key1=category, key2=subcategory)
        else:
            return HttpResponse("Subcategory not found")
    else:
        allitems = Items.objects.filter(key1=category)
    category = Category.objects.all()
    products = Products.objects.get()
    
    context = {
        'category':category,
        'allitems':allitems,
        'products':products,
        'categories': Category.objects.all()
    }
    MainInfoF(context)
    MainInlcude(context)
    SaveItems_Id_F(request,context)
    return render(request,'shop.html', context)

#--------------------------------------------------------------
#-------------------------Contact------------------------------
#--------------------------------------------------------------

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
    
#--------------------------------------------------------------
#----------------------Product_Details-------------------------
#--------------------------------------------------------------

class Product_Details(DetailView):
    template_name = 'product-details.html'

    def get(self,request,id):
        mainitem = get_object_or_404(Items,pk = id)
        items = Items.objects.all()
        images = ItemsImages.objects.all()
        details = mainitem.items_details_rn.first()
        if request.user.is_authenticated:
            name = request.user.username
            email = request.user.email
        else:
            name = ''
            email = '' 
        form = ReviewForm()
  
        ratings = ReviewMessage.objects.filter(key=mainitem).values_list('rating', flat=True)
        countt = ReviewMessage.objects.filter(key=mainitem).count()
        
        if ratings: 
            rate = math.ceil(sum(ratings) / len(ratings)) if sum(ratings) / len(ratings)%1 > 0.5 else int(sum(ratings) / len(ratings))
        else:
            rate = 0

        context = {
            'details':details,
            'rate':rate,
            'form':form,
            'name':name,
            'email':email,
            'mainitem':mainitem,
            'items':items,
            'images':images,
            'countt':countt,
        }
        MainInfoF(context)
        SaveItems_Id_F(request,context)
        return render(request,self.template_name,context)
    
    def post(self,request,id):
        form = ReviewForm(request.POST)
        messagee = ''
        if form.is_valid():
            review = form.save()
            if review.rating > 3:
                message = 'Thank you for your positive review!'
            else:
                message = "We appreciate your feedback and will work on improvements."
            email = EmailMessage(
                subject = f'Unswer to your review {request.POST.get('username')}',
                body = message,
                from_email=EMAIL_HOST_USER,
                to=[request.POST.get('email')]
            )
            email.send()
            return redirect('product_details',id = id) 
        else:
            messagee = form.errors
        context = {
            'form':form,
            'messagee':messagee,
        }
        MainInfoF(context)
        return render(request,self.template_name,context)
    
#--------------------------------------------------------------
#--------------------------Cart--------------------------------
#--------------------------------------------------------------

class CartPage(ListView):
    template_name = 'cart.html'

    def get(self,request,id):
        userr = get_object_or_404(User, pk = id)
        taxes = Total_payment.objects.get()
        saved_in_cart = UserSave.objects.filter(user_id = userr)
        total = 0
        dct = {}
        for i in saved_in_cart:
            dct[i] = i.item_id.price * i.quantity
        total_price = 0
        for i in saved_in_cart:
            total_price += i.item_id.price * i.quantity
        total = total_price
        total += taxes.Eco_Tax + taxes.Shipping_Cost

        context = {
            'total':total,
            'taxes':taxes,
            "dct":dct,
            'total_price':total_price
        }
        MainInfoF(context)
        return render(request,self.template_name,context)
    

def Item_Quantity_Add(request,user_id,item_id):
    userr = get_object_or_404(User, pk = user_id)
    itemm = get_object_or_404(UserSave,user_id = userr,item_id = item_id)
    if itemm.quantity >= 10:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        itemm.quantity += 1
        itemm.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

  
def Item_Quantity_Remove(request,user_id,item_id):
    userr = get_object_or_404(User, pk = user_id)
    itemm = get_object_or_404(UserSave,user_id = userr,item_id = item_id)
    if itemm.quantity <= 1:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        itemm.quantity -= 1
        itemm.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def UserSaveF(request,user_id,item_id):
    userr = get_object_or_404(User, pk=user_id)
    itemm = get_object_or_404(Items, pk=item_id)
    found = UserSave.objects.filter(user_id = userr, item_id = itemm)
    if found:
        UserSave.objects.get(user_id = userr, item_id = itemm).delete()
    else:
        UserSave.objects.create(user_id = userr, item_id = itemm)

    return redirect(request.META.get('HTTP_REFERER', '/'))


def SaveItems_Id_F(request,context):
    if request.user.is_authenticated:
        userr = get_object_or_404(User, pk = request.user.id)
        id_saver = []
        usersave = UserSave.objects.filter(user_id = userr)
        for i in usersave:
            id_saver.append(i.item_id.id)
        context['id_saver'] = id_saver

#--------------------------------------------------------------
#-------------------------ForgotPage---------------------------
#--------------------------------------------------------------

def ForgotPage(request):
    username = request.POST.get('username')
    if username:
        return redirect('redirect_middle',username)
    context = {

    }
    MainInfoF(context)
    return render(request,'forgotpage.html',context)


def RedirectMidddle(request,username):
    user_id = User.objects.filter(username = username).first().id
    userr = get_object_or_404(User,pk = user_id)
    uid = urlsafe_base64_encode(force_bytes(userr.pk))
    token = default_token_generator.make_token(userr)
    number = random.randint(1000,9999)
    UserFor.objects.update_or_create(key = userr,ver_code = number)
    email = User.objects.filter(username = username).first().email

    email_message = EmailMessage(
        subject='Verify to change password',
        body=f'This is your ferification code {number}',
        from_email=EMAIL_HOST_USER,
        to = [email]
    )
    email_message.send()
    return redirect('codecheck',uid,token)


def DighitalPage(request,uidb64, token):
    uid = urlsafe_base64_decode(uidb64).decode()
    userr = get_object_or_404(User,pk = uid)
    token = default_token_generator.make_token(userr)
    uid = urlsafe_base64_encode(force_bytes(userr.pk))
    username = userr.username
    ver_code_db = int(UserFor.objects.filter(key = userr).first().ver_code)
    if default_token_generator.check_token(userr, token):
        if request.method == 'POST':
            ver_code_user = int(request.POST.get('ver_code'))
            if ver_code_user == ver_code_db:
                UserFor.objects.filter(key = userr).delete()
                return redirect('reset',uidb64 = uid,token =  token)
    return render(request,'codecheck.html')


def PasswordReset(request,uidb64, token):
    uid = urlsafe_base64_decode(uidb64).decode()
    userr = get_object_or_404(User,pk = uid)

    reset_message = ''
    if request.method == 'POST':
        new_password = request.POST.get('password1')
        new_password_2 = request.POST.get('password2')
        if new_password == new_password_2:
            userr.set_password(new_password)
            userr.save()
            return redirect('login')
        else:
            reset_message = 'Passwords are not the same'
    context = {
        'reset_message':reset_message,
        }
    MainInfoF(context)
    return render(request,'passwordreset.html',context)


#--------------------------------------------------------------
#--------------------------------------------------------------
#--------------------------------------------------------------

