from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostView.as_view(), name="home"),
    path("team/", views.TeamView.as_view(), name="team"),
    path("portfolio/", views.PortfolioView.as_view(), name="portfolio"),
    path("service/", views.ServiceView.as_view(), name="service"),
    path("posts/<str:ct_model>/<str:slug>/", views.PostDetailView.as_view(), name="post_detail")
]