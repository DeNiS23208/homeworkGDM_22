# catalog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # ← обязательно .FILES
        if form.is_valid():
            form.save()
            return redirect('catalog:product_list')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # ← обязательно .FILES
        if form.is_valid():
            form.save()
            return redirect('catalog:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'catalog/product_form.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('catalog:product_list')
    return render(request, 'catalog/product_confirm_delete.html', {'product': product})
