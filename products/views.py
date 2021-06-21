from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, Http404
from .forms import ProductForm, ProductFormRaw
from .models import Product
from django.views.generic import ListView,DetailView, CreateView, DeleteView
from django.urls import reverse
from django.views import View

def home_view(request, *args, **kwargs):
    context = {
        'my_number': 910,
        'my_address': 'tehran',
        'title': 'Home',
        'my_phone_numbers':[
                912,938,267,652,902
        ]

    }
    return render(request,'home.html',context)

def about_view(request):
    context={
        'title':'About'
        }
    return render(request, 'about.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request,'product_create.html', context)
# def product_create_view(request):
#     form = ProductFormRaw()
#     if request.method == 'POST':
#         form = ProductFormRaw(request.POST)
#         if form.is_valid():
#             Product.objects.create(**form.cleaned_data)
#             form = ProductFormRaw()
#     context = {
#         'form': form
#     }
#     return render(request,'product_create.html', context)

def product_list_view(request):
    queryset = Product.objects.all()
    context={
        'objects': queryset,
    }
    return render(request,'product_list_view.html', context)

class ProductRawListView(View):
    def get(self, request, id=None):
        if id:
            obj = get_object_or_404(Product, id=id)
        context = {
        'obj': obj,
        }
        return render(request,'product_detail.html', context)
        

def product_detail_view(request,id):
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    obj = get_object_or_404(Product, id=id)
    context = {
        'obj': obj,
    }
    return render(request,'product_detail.html', context)

def product_delete_view(request,id):
    obj = Product.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../")
    context = {
        'obj': obj,
    }
    return render(request,'product_delete.html', context)

def product_update_view(request,id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request,'product_create.html', context)
    

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list_view.html'

class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    # queryset = Product.objects.all()
    def get_object(self, *args, **kwargs):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Product, id=id_)

class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = '/'

    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'

    def get_object(self, *args, **kwargs):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Product, id=id_)

    def get_success_url(self):
        return reverse('product:product_list')
