from django.shortcuts import render
from django.http  import HttpResponse
# Django 中，generic 是一個提供了通用（generic）模組
# 這些是 Django 框架中的一個重要功能，它們為你提供了一種簡化和快速創建畫面的方式，尤其是在處理 CRUD（創建、讀取、更新、刪除）操作時非常方便
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employer, Store, Product

# Create your views here.

def hello_world(request):
    return HttpResponse('hello')

def index(request):
    return render(request, 'index.html')

# region: employer

class EmployerListView(generic.ListView):
    """
    再來設定 EmployerListView，這個類別的來由就是我們剛剛路徑那邊設定的關係，而後面帶的參數(generic.ListView)，則是 Django 提供我們快速建置的方法
    最後設定這個 view 的 model 是 Employer (這個設定會影響到之後在 template 使用的變數、顯示的物件)
    """
    model = Employer
    
class EmployerDetailView(generic.DetailView):
    model = Employer
    
class EmployerCreate(CreateView):
    model = Employer
    fields = '__all__'
    success_url = reverse_lazy('employer-list')
    
class EmployerUpdate(UpdateView):
    model = Employer
    fields = '__all__'
    success_url = reverse_lazy('employer-list')
    
class EmployerDelete(DeleteView):
    model = Employer
    success_url = reverse_lazy('employer-list')
    
# endregion: employer

# region: store

class StoreListView(generic.ListView):
    model = Store
    
class StoreDetailView(generic.DetailView):
    model = Store
    
class StoreCreate(CreateView):
    model = Store
    fields = '__all__'
    success_url = reverse_lazy('store-list')
    
class StoreUpdate(UpdateView):
    model = Store
    fields = '__all__'
    success_url = reverse_lazy('store-list')
    
class StoreDelete(DeleteView):
    model = Store
    success_url = reverse_lazy('store-list')
    
# endregion: store

# region: product

class ProductListView(generic.ListView):
    model = Product
    
class ProductDetailView(generic.DetailView):
    model = Product
    
class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product-list')
    
class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product-list')
    
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')
    
# endregion: product
