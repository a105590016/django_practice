from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello_world, name='hello_world'),
    path('', views.index, name='index'),
    # employer
    path('employers', views.EmployerListView.as_view(), name='employer-list'),
    path('employer/<int:pk>', views.EmployerDetailView.as_view(), name='employer-detail'),
    path('employer/create', views.EmployerCreate.as_view(), name='employer-create'),
]
