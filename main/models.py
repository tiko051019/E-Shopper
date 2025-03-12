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
    add = models.ImageField('Addvertisement',upload_to='Images',null=True,blank=True)

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
        return self.subname
    
    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

class ItemsName(models.Model):
    name = models.CharField('Items name(category)',max_length=255)

    def __str__(self):
        return self.name

class Items(models.Model):
    key1 = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_rn')
    key2 = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name='subcat_rn',null=True,blank=True)
    key3 = models.ForeignKey(ItemsName,on_delete=models.CASCADE,related_name='itemsname_rn',null = True)
    price = models.IntegerField('Price')
    img = models.ImageField('Image',upload_to='Images')
    info = models.TextField('Info')
    brand = models.CharField('Brand',max_length=30)
    reccomend_bool = models.BooleanField('Reccom. or not',default=False)
    discount = models.IntegerField('Discount')
    disc_icon = models.ImageField('Discount Icon',null=True)

    def __str__(self):
        return 'Item'
    
class Gallery(models.Model):
    img = models.ImageField('Image',upload_to='Images')
    desc = models.TextField('Description',null=True)
    date = models.CharField('Date',max_length=30,null=True)

    def __str__(self):
        return 'Footer Gallery'