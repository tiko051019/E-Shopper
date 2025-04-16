from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import json
from django.shortcuts import render,get_object_or_404
from main.models import *
from django.utils import timezone
from django.utils.timezone import  timedelta
from django.contrib.auth.decorators import user_passes_test


def superuser_required(request):
    return user_passes_test(lambda u: u.is_superuser,'pagee404')(request)

@superuser_required
def DashbordHomeView(request):
    users_count = UsersRegisteringCountinMonth.objects.all()[UsersRegisteringCountinMonth.objects.all().count()-12:]
    my_list,my_list_months = [],[]    
    for i in users_count:
        my_list.append(i.Count)
        my_list_months.append(i.Month[:3])
    my_list.reverse()
    my_list_months.reverse()

    obj = get_object_or_404(DashboardInfo,pk = 1)
    obj.Users = User.objects.all().count()
    obj.save()
    
    dashboard_info = DashboardInfo.objects.get()
    armenian_time = timezone.localtime(timezone.now())
    five_minutes_ago =  armenian_time - timedelta(seconds=5)
    active_users_count = UserActivity.objects.filter(last_activity__gte=five_minutes_ago).count()

    print("Time five minutes ago:", five_minutes_ago)
    print("Active users count:", active_users_count)
    sum_list = [sum(my_list[:4]),sum(my_list[4:8]),sum(my_list[8:])]
    context = {
        'my_list':my_list,
        'my_list_2':json.dumps(my_list_months),
        'dashboard_info':dashboard_info,
        'active_users_count':active_users_count,
        'sum_list':sum_list,
            }
    

    return render(request,'index_dashboard.html',context)


def get_active_users_count(request):
    armenian_time = timezone.localtime(timezone.now())
    thirty_seconds_ago = armenian_time - timedelta(seconds=30)
    active_users_count = UserActivity.objects.filter(last_activity__gte=thirty_seconds_ago).count()

    return JsonResponse({"active_users_count": json.dumps(active_users_count)})

def pagee404(request):
    return render(request,'page404.html')