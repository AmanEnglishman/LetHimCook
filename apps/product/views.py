from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import ListView

from .forms import ReviewForm, RatingForm
from .models import Product, ProductImage, ProductSpecifications, Category, Rating


def index(request, category_if=None):
    context = {'products': Product.objects.all(),
               'product_images': ProductImage.objects.all(),
               'categories': Category.objects.all()}
    return render(request, 'index.html', context)


class DetailView(generic.DetailView):
    model = Product
    template_name = 'product/detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['star_form'] = RatingForm()
        context['product_images'] = product.images.all()
        context['specifications'] = product.specifications.filter(product=product)
        return context


def products_in_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)  # Подставьте свои реальные поля
    return render(request, 'index.html', {'category': category, 'products': products})


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())


class AddStarRating(View):

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                product_id=int(request.POST.get("product")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class Search(ListView):
    paginate_by = 3
    template_name = 'product/product_list.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Product.objects.filter(name__icontains=query)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context