from django.shortcuts import render
from django.views.generic import View, DetailView

from .models import *


class PostView(View):
    """Вывод постов на главной странице"""
    def get(self, request):
        service = Service.objects.all()
        portfolio = Portfolio.objects.all()
        helpbiz = Helpbiz.objects.all()
        stats = Statistic.objects.all()
        return render(request, "post_list.html", {
            "service_list": service, "portfolio_list": portfolio, "help_list": helpbiz, "static_list": stats
        })


class PostDetailView(DetailView):
    CT_MODEL_MODEL_CLASS = {
        'service': Service,
        'portfolio': Portfolio
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'post'
    template_name = 'post_detail.html'
    slug_url_kwarg = 'slug'


class TeamView(View):
    """Вывод команды на странице Team"""
    def get(self, request):
        team = Team.objects.all()
        return render(request, "team.html", {"team_list": team})
