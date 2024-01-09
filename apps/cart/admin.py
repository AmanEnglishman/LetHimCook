from django.contrib import admin

from .models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )
    list_display_links = (
        'id',
    )
    list_filter = (
        'id',
    )
    search_fields = (
        'id',
    )

