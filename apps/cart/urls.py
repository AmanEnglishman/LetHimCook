from django.urls import path

from .views import (cart_add,
                    cart_view,
                    cart_delete,
                    cart_quantity_minus,
                    wishlist_view,
                    wishlist_add,
                    wishlist_delete,
                    cart_delete_all)

urlpatterns = [
    path('', cart_view, name='cart-view'),
    path('cart_add/<int:product_id>/', cart_add, name='cart-add'),
    path('cart_delete/<int:id>/', cart_delete, name='cart-delete'),
    path('cart_delete_all', cart_delete_all, name='cart-delete-all'),
    path('cart_minus/<int:product_id>', cart_quantity_minus, name='cart-quantity-minus'),
    path('wishlist_add/<int:product_id>/', wishlist_add, name='wishlist-add'),
    path('wishlist/', wishlist_view, name='wishlist-view'),
    path('wishlist_delete/<int:id>/', wishlist_delete, name='wishlist-delete'),

]
