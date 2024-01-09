from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from .models import Basket, Wishlist
from apps.product.models import Product


def cart_view(request):

    carts = Basket.objects.filter(user=request.user)
    total_quantity = sum(cart.quantity for cart in carts)
    total_sum = sum(cart.sum() for cart in carts)

    return render(request, 'cart/cart.html',
                  {'carts': carts,
                   'total_quantity': total_quantity,
                   'total_sum': total_sum}, )


def cart_add(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    carts = Basket.objects.filter(user=user, product=product)

    if not carts.exists():
        Basket.objects.create(user=user, product=product, quantity=1)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_delete(request, id):
    cart = Basket.objects.get(id=id)
    cart.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_delete_all(request):
    cart = Basket.objects.all()
    cart.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_quantity_minus(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    carts = Basket.objects.filter(user=user, product=product)

    if carts.exists():
        cart = carts.first()
        cart.quantity -= 1
        cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def wishlist_view(request):
    wishlists = Wishlist.objects.filter(user=request.user)

    return render(request, 'cart/wishlist.html', {'wishlists': wishlists})


def wishlist_add(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    wishlists = Wishlist.objects.filter(user=user, product=product)

    if not wishlists.exists():
        Wishlist.objects.create(user=user, product=product)
    else:
        cart = wishlists.first()
        cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def wishlist_delete(request, id):
    wishlist = Wishlist.objects.get(id=id)
    wishlist.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

