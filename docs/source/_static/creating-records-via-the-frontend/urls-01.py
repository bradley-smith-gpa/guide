from django.urls import path
from orders.views import CustomerCreateView


urlpatterns = [
    path(
        'customer/create/', CustomerCreateView.as_view(),
        name='customer-create'
    ),
]
