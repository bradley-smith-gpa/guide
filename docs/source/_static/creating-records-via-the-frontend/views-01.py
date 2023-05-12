from django.views.generic import CreateView
from django.urls import reverse_lazy
from orders.models import Customer
from orders.forms import CustomerCreateForm


class CustomerCreateView(CreateView):
    template_name = 'orders/customer-create/customer-create.html'
    model = Customer
    form_class = CustomerCreateForm
    success_url = reverse_lazy('home-template')
