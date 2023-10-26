from django.shortcuts import render
from django.http  import HttpResponse
# Django 中，generic 是一個提供了通用（generic）模組
# 這些是 Django 框架中的一個重要功能，它們為你提供了一種簡化和快速創建畫面的方式，尤其是在處理 CRUD（創建、讀取、更新、刪除）操作時非常方便
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employer

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
    
class EmployerCreate(CreateView):
    model = Employer
    fields = '__all__'
    success_url = reverse_lazy('employer-list')
    
# endregion: employer