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
    
class Carousel(models.Model):
    text1 = models.TextField('text1')
    text2 = models.TextField('text2')
    img = models.ImageField('Girls image',upload_to='Images')
    disc_img = models.ImageField('Discount image',upload_to='Images')

    def __str__(self):
        return 'Carousel'
    
    class Meta:
        verbose_name = 'Main Info'
        verbose_name_plural = 'Main Info'
    
class Category(models.Model):
    name = models.CharField('Category name',max_length=50)
    sub_bool = models.BooleanField('Has sub. or not',default=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
class SubCategory(models.Model):
    key = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='subcat_rn')
    subname = models.CharField('Category name',max_length=50)

    def __str__(self):
        return f'{self.key}'
    
    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'