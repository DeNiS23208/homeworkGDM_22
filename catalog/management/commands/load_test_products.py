from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Загружает тестовые продукты, предварительно очищая базу'

    def handle(self, *args, **kwargs):
        self.stdout.write("Удаляю старые продукты и категории...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        laptops = Category.objects.create(name="Ноутбуки", description="Тестовая категория")
        phones = Category.objects.create(name="Смартфоны", description="Тестовая категория")

        Product.objects.create(name="Test Laptop", description="Описание", category=laptops, price=1000)
        Product.objects.create(name="Test Phone", description="Описание", category=phones, price=500)

        self.stdout.write(self.style.SUCCESS("Тестовые данные успешно загружены!"))
