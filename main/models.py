from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


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
        return self.brand

class Products(models.Model):
    add = models.ImageField('Rec_add_img',upload_to='Images')

    def __str__(self):
        return 'Products_page_field'




class ItemsDetails(models.Model):
    key = models.ForeignKey(Items,on_delete=models.CASCADE,related_name='items_details_rn')
    moreinfo = models.TextField('Description')
    availability = models.BooleanField('Availability')
    condition = models.BooleanField('Condition')
    condition_img = models.ImageField('Logo <New>',upload_to='Images',null=True)

    def __str__(self):
        return f'{self.key}'

    class Meta:
        verbose_name = 'ItemDetails'
        verbose_name_plural = 'ItemsDetails'

class ItemsImages(models.Model):
    key = models.ForeignKey(Items,on_delete=models.CASCADE,related_name='items_images_rn')
    img = models.ImageField('Carousel Images',upload_to='Images')

    def __str__(self):
        return f'{self.key}'



class Gallery(models.Model):
    img = models.ImageField('Image',upload_to='Images')
    desc = models.TextField('Description',null=True)
    date = models.CharField('Date',max_length=30,null=True)

    def __str__(self):
        return 'Footer Gallery'
    


class ContactMessage(models.Model):
    name = models.CharField('Name',max_length=50)
    email = models.EmailField('Email')
    subject = models.CharField('Subject',max_length=255)
    message = models.TextField('Message')

    def __str__(self):
        return f'{self.name} message'
    

class ReviewMessage(models.Model):
    key = models.ForeignKey(Items,on_delete=models.CASCADE,related_name='reviews_rn',null = True, blank = True)
    name = models.CharField('Name',max_length=50)
    email = models.EmailField('Email')
    message = models.TextField('Message') 
    CHOICES = [(1, 'One'),(2, 'Two'),(3, 'Three'),(4, 'Four'),(5, 'Five'),]
    rating = models.IntegerField(choices=CHOICES, default = 5, null=True,blank=True)
