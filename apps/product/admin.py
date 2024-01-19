from django.contrib import admin

from .models import (Product,
                     ProductImage,
                     ProductSpecifications,
                     Brand,
                     BrandModel,
                     Reviews,
                     RatingStar,
                     Rating)


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecifications


class ProductImageSpecificationInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSpecificationInline, ProductImageSpecificationInline]
    list_display = (
        'id',
        'name'
    )
    list_display_links = (
        'name',
        'id'
    )
    list_filter = (
        'name',
        'id'
    )
    search_fields = (
        'name',
        'id'
    )


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Reviews)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(RatingStar)
class CategoryAdmin(admin.ModelAdmin):
    pass
