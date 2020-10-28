from django.forms import ModelChoiceField, ModelForm, ValidationError
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *
from django.contrib.flatpages.models import FlatPage
# Примечание: мы переименовываем исходные Admin и Form по мере их импорта!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld


class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="Описание")

    class Meta:
        model = FlatPage  # это не наследуется автоматически от FlatpageFormOld
        fields = '__all__'


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm


# Мы должны отменить регистрацию обычного администратора, а затем перерегистрировать нашего
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


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
    list_display = ("title", "date", "link_project", "category", "slug")


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
    list_display = ("title", "category", "age", "slug")


@admin.register(Helpbiz)
class HelpbizAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ("title", "backg")


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ("title", "number")


admin.site.site_title = "Enigma.kg"
admin.site.site_header = "Enigma.kg"
