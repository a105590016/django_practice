from django.db import models
from django.urls import reverse

# Create your models here.

class Employer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    
    class Meta:
        """
        class Meta
        
        這裡的 Meta 方法，可用來控制模型的行為和屬性，像是 Model 的排列順序和權限設定之類的事情
        """
        # 先依照 last_name 排列，接著在按照 first_name 排列
        ordering = ['last_name', 'first_name']
        
    def get_absolute_url(self):
        """
        回傳 url name='employer-detail' 的連結, detail 要再加上 id
        """
        return reverse('employer-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.first_name}-{self.last_name}'
    
    
class Store(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)
    
    def get_obsolute_url(self):
        return reverse('store-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=100)
    store = models.ManyToManyField(Store)
    
    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title
    
    
class StoreProduct(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)