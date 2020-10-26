from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostView.as_view(), name="home"),
    path("team/", views.TeamView.as_view(), name="team"),
]