from django.shortcuts import redirect
from django.views import generic

from phones.models import Phone


def home(request):
    return redirect('catalog/')


class Catalog(generic.ListView):
    model = Phone
    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_ordering(self):
        return self.request.GET.get('sort')


class Product(generic.DetailView):
    model = Phone
    template_name = 'product.html'
    context_object_name = 'product'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context