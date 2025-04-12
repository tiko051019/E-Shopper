from django.shortcuts import render
import json

def DashbordHomeView(request):
    my_list = [100,50,20,10,50,60,70,80,90,80,70,60]

    context = {
        'my_list':my_list,
              }

    return render(request,'index_dashboard.html',context)