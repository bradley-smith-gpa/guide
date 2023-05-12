from django.urls import path
from orders.views import (
    CustomerCreateView, CustomerListView, ProductCreateView, OrderCreateView
)


urlpatterns = [
    path(
        'customer/create/', CustomerCreateView.as_view(),
        name='customer-create'
    ),
    path(
        'customer/list/', CustomerListView.as_view(),
        name='customer-list'
    ),
    path(
        'product/create/', ProductCreateView.as_view(),
        name='product-create'
    ),
    path(
        'order/create/', OrderCreateView.as_view(),
        name='order-create'
    ),
]
