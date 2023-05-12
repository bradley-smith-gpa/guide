from django.views.generic import TemplateView


class HomeTemplate(TemplateView):
    template_name = 'basics/home-template/home-template.html'


class AboutTemplate(TemplateView):
    template_name = 'basics/about-template/about-template.html'


class ContactTemplate(TemplateView):
    template_name = 'basics/contact-template/contact-template.html'
    

