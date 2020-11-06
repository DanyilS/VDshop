from django.shortcuts import render, get_object_or_404

from .models import Product


def home(request):
    return render(request, "store/home.html")


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    # TODO: write template "store/templates/store/product_detail.html"
    return render(request, '', context=context)
