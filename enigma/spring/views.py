from django.shortcuts import render
from django.views.generic import View

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


class TeamView(View):
    """Вывод команды на странице Team"""
    def get(self, request):
        team = Team.objects.all()
        return render(request, "team.html", {"team_list": team})
