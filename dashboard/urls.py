from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard_home/',DashbordHomeView,name='dashboard_home'),
    path('api/active-users/', get_active_users_count, name='get_active_users_count'),
    path('page_404/',pagee404,name='pagee404')
]