from django.core.management.base import BaseCommand
from django.core.cache import cache

class Command(BaseCommand):
    help = "Тестирование кеша Redis"

    def handle(self, *args, **kwargs):
        cache.set('test_key', 'Мира любит тебя 💖', timeout=60)
        value = cache.get('test_key')
        self.stdout.write(f"Значение из кеша: {value}")
