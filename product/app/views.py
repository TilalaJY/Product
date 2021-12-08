from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.db.models import Q, fields
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin


from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

from .forms import *

from .models import *

# Create your views here.

class ProductView(TemplateView):
    template_name = "product/product.html"

class ProductCreateView(SuperuserRequiredMixin, CreateView):
    model = Product
    fields = [ 'Name', 'product_code', 'price', 'category', 'manufacture_date', 'expiry_date', 'owner']
    template_name = "product/product_add.html"
    
    def get_success_url(self):
        return reverse_lazy("index")

class ProductUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Product
    fields = [ 'Name', 'product_code', 'price', 'category', 'manufacture_date', 'expiry_date', 'owner']
    template_name = "product/product_update.html"
    
    def get_success_url(self):
        return reverse_lazy("index")

class ProductDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Product
    template_name = "product/product_delete.html"
    success_url = '/'


class ProductList(BaseDatatableView):
    model = Product
    columns = ["id", 'Name', 'product_code', 'price', 'category', 'manufacture_date', 'expiry_date', 'owner', 'flag']
    order_columns = ["id",'Name', 'product_code', 'price', 'category', 'manufacture_date', 'expiry_date', 'owner', 'flag']

    def render_column(self, row, column): 
        if column == 'owner':
            return escape('{0} {1}'.format(row.owner.first_name, row.owner.last_name))
        elif column == 'flag':
            return self.request.user.is_superuser
        else:
            return super(ProductList, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(Name__icontains=search))
        return qs

class CategoryView(TemplateView):
    template_name = "product/category.html"

class CategoryCreateView(SuperuserRequiredMixin, CreateView):
    model = Category
    fields = ['category', 'sub_category']
    template_name = "product/category_add.html"
    
    def get_success_url(self):
        return reverse_lazy("category-index")

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['category', 'sub_category']
    template_name = "product/category_update.html"
    def get_success_url(self):
        return reverse_lazy("category-index")

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "product/category_delete.html"
    success_url = '/'


class CategoryList(BaseDatatableView):
    model = Category
    columns = ['id','category', 'sub_category', 'flag']
    order_columns = ['id', 'category', 'sub_category', 'flag']

    def render_column(self, row, column):
        if column == 'flag':
            return self.request.user.is_superuser
        else:
            return super(CategoryList, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(category__icontains=search))
        return qs


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="sign_up.html", context={"register_form":form})
