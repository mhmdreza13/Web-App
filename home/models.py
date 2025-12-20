from django.db import models

# Create your models here.

class Category (models.Model):

    name = models.CharField(max_length = 100)
    create = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = 'category')

    def __str__(self):
        return self.name
    


class Product (models.Model):
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    category = models.ForeignKey(Category ,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,verbose_name='نام')
    amount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True ,null=True)
    total_price = models.PositiveIntegerField()
    information = models.TextField(blank=True ,null=True)
    create = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    available = models.BooleanField(default = True)
    image = models.ImageField(upload_to = 'product')

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