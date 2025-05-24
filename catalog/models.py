from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        default=1
    )

    class Meta:
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]

    def __str__(self):
        return self.name
