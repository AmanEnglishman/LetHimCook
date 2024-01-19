from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import ListView

from .forms import ReviewForm, RatingForm
from .models import Product, ProductImage, ProductSpecifications, Rating, Brand, Reviews


def index(request):
    context = {'products': Product.objects.all(),
               'category_list': Brand.objects.all()}

    return render(request, 'index.html', context)


def filter_by_category(request, id):
    objects = Product.objects.filter(brand_id=id)
    categories = Brand.objects.all()
    return render(request, 'index.html', context={
        'products': objects,
        'category_list': categories,
    }
                  )


# class DetailView(generic.DetailView):
#     model = Product
#     template_name = 'product/detail_view.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         product = self.get_object()
#         context['star_form'] = RatingForm()
#         context['product_images'] = product.images.all()
#         context['specifications'] = product.specifications.filter(product=product)
#         return context


def product_detail(request, pk):
    object = Product.objects.get(id=pk)
    reviews = Reviews.objects.filter(product_id=pk)
    if request.method == 'POST':
        reviews = Reviews.objects.create(
            user_id=request.user.id,
            product_id=pk,
            text=request.POST['text']
        )
        reviews.save()
        return redirect('product-detail', pk)
    return render(request, 'product/detail_view.html', {
        'object': object,
        'reviews': reviews
    })


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


def comment_delete(request, id):
    reviews = Reviews.objects.get(id=id)
    reviews.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
