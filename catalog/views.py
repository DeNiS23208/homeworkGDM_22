from idlelib.debugobj import dispatch

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from .models import Product
from .forms import ProductForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .services.product_services import get_products_by_category


def products_by_category(request, category_id):
    products = get_products_by_category(category_id)
    return render(request, 'catalog/products_by_category.html', {'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})


@cache_page(60 * 15)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


@login_required(login_url='users:login')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user  # 👈 Привязка владельца
            product.save()
            return redirect('catalog:product_list')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})


@login_required(login_url='users:login')
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.owner != request.user:
        return HttpResponseForbidden("Редактировать может только владелец.")  # 👈 Ограничение

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'catalog/product_form.html', {'form': form})


@login_required(login_url='users:login')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    is_moderator = request.user.groups.filter(name='Модератор продуктов').exists()

    if product.owner != request.user and not is_moderator:
        return HttpResponseForbidden("Удалять может только владелец или модератор.")  # 👈 Ограничение

    if request.method == 'POST':
        product.delete()
        return redirect('catalog:product_list')
    return render(request, 'catalog/product_confirm_delete.html', {'product': product})


@login_required(login_url='users:login')
@permission_required('catalog.can_unpublish_product', raise_exception=True)
def product_unpublish(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_published = False
    product.save()
    return redirect('catalog:product_detail', pk=pk)
