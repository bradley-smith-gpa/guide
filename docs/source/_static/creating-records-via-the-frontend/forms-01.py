from django.forms import ModelForm
from orders.models import Customer, Product, Order


class StyledModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # remove default colon after label within `label_tag`
        self.label_suffix = ''
        # add Bootstrap class attribute to widget for all fields
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class CustomerCreateForm(StyledModelForm):

    class Meta:
        model = Customer
        fields = ['first_name', 'middle_name', 'last_name', 'email']

    template_name = 'orders/customer-create/form.html'
