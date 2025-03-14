from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_register_view,name='login'),
    path('logout/',Logout,name='logout'),
    path('home/',HomeListView.as_view(),name='home'),
    path('products/',ProductsPage.as_view(),name='products'),
    path('contact/',ContactPage.as_view(),name='contact'),
    path('filter/<str:category_name>/<str:subcategory_name>/',filter_products,name='filter'),
    path('filter/<str:category_name>/',filter_products,name='filter_c'),

    
]