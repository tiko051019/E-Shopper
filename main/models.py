from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class MainInfo(models.Model):
    name = models.CharField('Site name',max_length=30)
    phone = PhoneNumberField('Phone')
    email = models.EmailField('Email')
    facebook = models.URLField("Faceboook")
    twitter = models.URLField('Twitter')
    linkedin = models.URLField('LinkedIn')
    dribbble = models.URLField('Dribbble')
    googleplus = models.URLField('Google Plus')
    img = models.ImageField('Logoname',null = True)
    info = models.TextField('Text',null=True)
    owner = models.CharField('Owner',max_length=20,null=True)

    def __str__(self):
        return 'MainInfo'
    
