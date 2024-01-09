from django.urls import path

from .views import index, DetailView, products_in_category, all_categories, AddReview, AddStarRating, Search

urlpatterns = [
    path('', index, name='home'),
    path('<int:category_id>/', index, name='category'),
    path('category/<int:category_id>/', products_in_category, name='products_in_category'),
    path('all-categories/', all_categories, name='all_categories'),
    path('product/<int:pk>', DetailView.as_view(), name='product-detail'),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    path('add-rating/', AddStarRating.as_view(), name='add_star'),
    path('search/', Search.as_view(), name='search'),
]
