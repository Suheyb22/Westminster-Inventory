from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('inventoryManagement/', views.inventoryManagement, name='dashboard-inventoryManagement'),
    path('userManagement/', views.userManagement, name='dashboard-userManagement'),
    path('myAccount/', views.myAccount, name='dashboard-myAccount'),
]
