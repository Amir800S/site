from django.views.generic import TemplateView


class AboutCompany(TemplateView):
    """Шаблон раздела 'О компании'."""

    template_name = 'author.html'

class HowToOrder(TemplateView):
    """Шаблон раздела 'Как заказать'."""

    template_name = 'how_to_order.html'

class Contacts(TemplateView):
    """.Шаблон раздела 'Контакты'."""

    template_name = 'contact.html'