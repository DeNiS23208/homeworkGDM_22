from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


# catalog/models.py

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)

    def __str__(self):
        return self.name
