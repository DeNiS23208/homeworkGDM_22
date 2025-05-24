from catalog.models import Product
from django.core.cache import cache


def get_products_by_category(category_id):
    cache_key = f"products_in_category_{category_id}"
    products = cache.get(cache_key)

    if products is None:
        print("📦 Данные взяты из БД")
        products = list(Product.objects.filter(category__id=category_id, is_published=True))
        cache.set(cache_key, products, timeout=60 * 5)
    else:
        print("⚡ Данные взяты из кеша")

    return products
