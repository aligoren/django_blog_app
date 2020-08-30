from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = "auth/dashboard.html"
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    settings = { 'title': 'Dashboard', 'dashboard': 'container-fluid' }

    def get(self, request):

        

        context = { 'settings': self.settings }

        return render(request, self.template_name, context)