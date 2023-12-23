from django.views.generic import TemplateView

class DashboardPage(TemplateView):
    template_name = 'dashboard.html'

