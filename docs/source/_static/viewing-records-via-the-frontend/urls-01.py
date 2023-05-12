from django.urls import path
from orders.views import CustomerCreateView, CustomerListView


urlpatterns = [
    path(
        'customer/create/', CustomerCreateView.as_view(),
        name='customer-create'
    ),
    path(
        'customer/list/', CustomerListView.as_view(),
        name='customer-list'
    ),
]
