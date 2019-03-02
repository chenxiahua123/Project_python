from django.db import models

# Create your models here.

class Lunbo(models.Model):
    name=models.CharField(max_length=100)
    img=models.CharField(max_length=100)

    class Meta:
        db_table='蘑菇街_轮播图'


class Register(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    token=models.CharField(max_length=100)

    class Meta:
        db_table='蘑菇街_注册'

class Lunbo2(models.Model):
    name=models.CharField(max_length=100)
    img=models.CharField(max_length=100)

    class Meta:
        db_table='蘑菇街_轮播图2'


class Product(models.Model):
    img=models.CharField(max_length=100)
    price=models.IntegerField()
    marketprice=models.IntegerField()
    number=models.IntegerField()

    class Meta:
        db_table='蘑菇街_产品信息'


class Cart(models.Model):
    user=models.ForeignKey(Register)

    product=models.ForeignKey(Product)

    number=models.IntegerField()

    isselect=models.BooleanField(default=True)

    class Meta:
        db_table='蘑菇街_购物车'