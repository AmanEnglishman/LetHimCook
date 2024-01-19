from django.urls import path

from .views import index, AddStarRating, Search, filter_by_category, product_detail, comment_delete

urlpatterns = [
    path('', index, name='home'),
    path('<int:id>', filter_by_category, name=' filter-by-category'),
    path('product/<int:pk>', product_detail, name='product-detail'),
    path('add-rating/', AddStarRating.as_view(), name='add_star'),
    path('search/', Search.as_view(), name='search'),
    path('review-delete/<int:id>', comment_delete, name='review-delete')
]
