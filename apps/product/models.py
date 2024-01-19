from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')


class BrandModel(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('BrandModel')
        verbose_name_plural = _('BrandsModels')


class Product(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    description = models.TextField(
        _('Description'),
    )
    price = models.PositiveIntegerField(
        _('Price'),
        default=0,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='brand_products',
        verbose_name=_('Brand'),
    )
    brand_model = models.ForeignKey(
        BrandModel,
        on_delete=models.CASCADE,
        related_name='brand_model_products',
        verbose_name=_('Brand Model'),
    )
    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


class ProductSpecifications(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='specifications',
        verbose_name=_('Product'),
    )
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    value = models.CharField(
        _('Value'),
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product specification')
        verbose_name_plural = _('Product specifications')


class ProductImage(models.Model):
    image = models.ImageField(
        _('Image'),
        upload_to='products/',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Product'),
    )


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(_('Text'))
    product = models.ForeignKey(Product, verbose_name='product', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.product}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class RatingStar(models.Model):
    value = models.SmallIntegerField("Value", default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Star Value"
        verbose_name_plural = "Star Value"
        ordering = ["-value"]


class Rating(models.Model):
    ip = models.CharField("IP address", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="star")
    movie = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="product")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "RatingЯs"
