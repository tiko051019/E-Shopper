from django.db import models
import datetime
from django.contrib.auth.models import User

class UsersRegisteringCountinMonth(models.Model):
    Month = models.CharField('Month',max_length=20,default=f'{datetime.datetime.now().strftime('%B')}')
    Year = models.CharField('Year',max_length=20,default=f'{datetime.datetime.now().year}')
    Count = models.IntegerField('Registering count',default=0)

    def __str__(self):
        return f'{self.Year} - {self.Month}'
    
class DashboardInfo(models.Model):
    Value = models.FloatField('Value',default=0)
    Users = models.IntegerField('Users',default=0)
    Orders = models.IntegerField('Orders',default=0)

    def __str__(self):
        return 'Dashboard_Info'
    

class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(null=True, blank=True)

    def str(self):
        return f"{self.user.username} - {self.last_activity}"