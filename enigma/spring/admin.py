from django.forms import ModelChoiceField, ModelForm, ValidationError
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    save_on_top = True
    form = PostAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "date", "client_name", "category", "slug")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    save_on_top = True
    form = PostAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "category", "slug")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    save_on_top = True
    form = PostAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "category", "developer", "age", "slug")


@admin.register(Helpbiz)
class HelpbizAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ("title", "backg")


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ("title", "number")

