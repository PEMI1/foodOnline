from django.urls import  path
from accounts import views as AccountsViews
from . import views



urlpatterns = [
     path('', AccountsViews.custDashboard, name ='customer'),
     path('profile/', views.cprofile, name='cprofile'),
     path('my_orders/', views.my_orders, name='customer_my_orders'),
     path('order_detail/<str:order_number>/', views.order_detail, name='order_detail'),



]