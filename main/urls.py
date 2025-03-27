from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

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
    path('cart/<int:id>/',CartPage.as_view(),name='cart'),
    path('save/<int:user_id>/<int:item_id>/',UserSaveF,name = 'save_f'),
    path('forgot/',ForgotPage,name='forgot_1'),
    path('check_code/<str:username>/',RedirectMidddle,name = 'redirect_middle'),
    path('password_numbers/<uidb64>/<token>/',DighitalPage,name = 'codecheck'),
    path('password_reset/<uidb64>/<token>/',PasswordReset,name = 'reset'),
    path('add_item/<int:user_id>/<int:item_id>/',Item_Quantity_Add,name='add_quantity'),
    path('remove_item/<int:user_id>/<int:item_id>/',Item_Quantity_Remove,name='remove_quantity')
]