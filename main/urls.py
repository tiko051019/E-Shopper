from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# def custom_404(request, exception):
#     return render(request, '404.html', status=404)

handler404 = 'main.views.custom_404'

urlpatterns = [
    path('login/',login_register_view,name='login'),
    path('logout/',Logout,name='logout'),
    path('home/',HomeListView.as_view(),name='home'),
    path('products/',ProductsPage.as_view(),name='products'),
    path('contact/',ContactPage.as_view(),name='contact'),
    path('home/filter/<str:category_name>/<str:subcategory_name>/',filter_home_products,name='filter'),
    path('home/filter/<str:category_name>/',filter_home_products,name='filter_c'),
    path('products/filter_products/<str:category_name>/<str:subcategory_name>/',filter_products,name='filter_products'),
    path('products/filter_products/<str:category_name>/',filter_products,name='filter_products_c'),
    path('product-details/<int:id>/',Product_Details.as_view(),name='product_details'),
    path('cart/<uid>/<token>/',CartPage.as_view(),name='cart_page'),
    path('cart_encode/<int:id>/',cart_encode,name = 'cart'),
    path('save/<int:user_id>/<int:item_id>/',UserSaveF,name = 'save_f'),
    path('forgot/',ForgotPage,name='forgot_1'),
    path('check_code/<str:username>/',RedirectMidddle,name = 'redirect_middle'),
    path('password_numbers/<uidb64>/<token>/',DighitalPage,name = 'codecheck'),
    path('password_reset/<uidb64>/<token>/',PasswordReset,name = 'reset'),
    path('add_item/<int:user_id>/<int:item_id>/',Item_Quantity_Add,name='add_quantity'),
    path('remove_item/<int:user_id>/<int:item_id>/',Item_Quantity_Remove,name='remove_quantity'),
    path('success/',payment_success,name = 'success'),
    path('cancel/',payment_cancel,name = 'cancel'),
    path('account_encode/<int:id>/',account_encode,name='account'),
    path('account/<uid>/<token>/',Account_Page.as_view(),name = 'account_page'),
    path('remove_items/',remove_from_cart,name='remove_items'),
    path('page404/',page404,name='page404'),
    path('privacy_policy',privacy_policy,name='privacy')
]

