from django.db import models
from django.urls import reverse
# Create your models here.

class Category (models.Model):
    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصول'

    name = models.CharField(max_length = 100)
    create = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(allow_unicode = True ,unique = True ,null= True ,blank= True)
    update = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = 'category',null=True , blank= True)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE,blank=True , null= True,related_name='subcategory')
    is_sub_category = models.BooleanField (default= False)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("home:category", args=[self.slug,self.id])
    

class Product (models.Model):

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    VARIANT = (
        ('None' , 'هیچکدام'),
        ('Size' , 'اندازه'),
        ('Color','رنگ'),
    )

    category = models.ManyToManyField(Category,blank=True,verbose_name='گروه محصول')
    name = models.CharField(max_length=200,verbose_name='نام')
    amount = models.PositiveIntegerField(verbose_name='موجودی')
    unit_price = models.PositiveIntegerField(verbose_name='قیمت')
    discount = models.PositiveIntegerField(blank=True ,null=True,verbose_name='درصد تخفیف')
    total_price = models.PositiveIntegerField(verbose_name='قیمت نهایی')
    information = models.TextField(blank=True ,null=True,verbose_name='اطلاعات')
    create = models.DateTimeField(auto_now_add = True,verbose_name='تاریخ ایجاد')
    update = models.DateTimeField(auto_now = True,verbose_name='تارخ آخرین تغییر')
    available = models.BooleanField(default = True,verbose_name='در دسترس')
    status = models.CharField(max_length = 200,null = True , blank = True , choices = VARIANT )
    image = models.ImageField(upload_to = 'product',verbose_name='تصویر')

    def __str__(self):
        return self.name
    @property
    def total_price (self):
        if not self.discount:
            return self.unit_price
        elif self.discount :
            total = (self.discount * self.unit_price) / 100
            return int (self.unit_price - total)
        return 
    
class Size (models.Model):

    class Meta:
        verbose_name = 'اندازه'
        verbose_name_plural = 'اندازه'

    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
    

class Color (models.Model):

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ'

    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name 

class Variants (models.Model):
    name = models.CharField(max_length=100)
    product_variant = models.ForeignKey(Product ,on_delete=models.CASCADE)
    size_variant = models.ForeignKey(Size ,on_delete=models.CASCADE)
    color_variant = models.ForeignKey(Color ,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name='موجودی')
    unit_price = models.PositiveIntegerField(verbose_name='قیمت')
    discount = models.PositiveIntegerField(blank=True ,null=True,verbose_name='درصد تخفیف')
    total_price = models.PositiveIntegerField(verbose_name='قیمت نهایی')

    def __str__(self):
        return self.name
    @property
    def total_price (self):
        if not self.discount:
            return self.unit_price
        elif self.discount :
            total = (self.discount * self.unit_price) / 100
            return int (self.unit_price - total)
        return 