from django.db import models

# Create your models here.

class CostType(models.Model):
    name = models.CharField(max_length=100, verbose_name='ТИП')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название брэнда')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    cost = models.FloatField(verbose_name='Цена')
    cost_type = models.ForeignKey(CostType, null=True, on_delete=models.SET_NULL)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(null=True, default=None)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name + ": " + str(self.cost) + " " + self.cost_type.name
