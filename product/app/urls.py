from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
from .api import *

urlpatterns = [
    path('', login_required(ProductView.as_view()), name="index"),
    path('product-list/', login_required(ProductList.as_view()), name='product-list'),
    path('product-add/', login_required(ProductCreateView.as_view()), name='product-add'),
    path('product-update/<int:pk>', login_required(ProductUpdateView.as_view()), name='product-update'),
    path('product-delete/<int:pk>', login_required(ProductDeleteView.as_view()), name='product-delete'),
    
    path('category-index/', login_required(CategoryView.as_view()), name="category-index"),
    path('category-list/', login_required(CategoryList.as_view()), name='category-list'),
    path('category-add/', login_required(CategoryCreateView.as_view()), name='category-add'),
    path('category-update/<int:pk>', login_required(CategoryUpdateView.as_view()), name='category-update'),
    path('category-delete/<int:pk>', login_required(CategoryDeleteView.as_view()), name='category-delete'),
    
    # Rest-api for the Product
    path('api',ProductApi.as_view()),
    path('api/create',ProductCreateApi.as_view()),
    path('api/<int:pk>',ProductUpdateApi.as_view()),
    path('api/<int:pk>/delete',ProductDeleteApi.as_view()),

]