from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_register_view,name='login'),
    path('logout/',Logout,name='logout'),
    path('home/',HomeListView.as_view(),name='home'),
]