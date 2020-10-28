from django.db import models
from django.urls import reverse


def get_post_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.CharField(max_length=255, verbose_name="URL", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название")
    subtitle = models.CharField(max_length=255, verbose_name="Подзаголовок", blank=True, null=True)
    slug = models.CharField(max_length=255, verbose_name="URL", unique=True)
    image = models.ImageField(verbose_name="Фото", blank=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.title


class Portfolio(Post):
    link_project = models.CharField(max_length=255, verbose_name="Ссылка на проект", blank=True)
    project_cat = models.CharField(max_length=255, verbose_name="Технологии используемые в проекте", blank=True)
    date = models.CharField(max_length=255, verbose_name="Дата создания проекта", blank=True)
    speed = models.CharField(
        verbose_name="Скорость выхода поста", max_length=50, blank=True, null=True,
        help_text="Выбрать один из скоростей: 0.2, 0.4, 0.6"
    )

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"

    def get_absolute_url(self):
        return get_post_url(self, 'post_detail')


class Service(Post):
    photo = models.ImageField(verbose_name="Фото", blank=True)
    backg = models.CharField(
        verbose_name="Background слайдера на главной стр", max_length=255, blank=True, null=True,
        help_text="Выбрать один из цветов для фона: a, b, c, d, e, f"
    )
    back_fon = models.CharField(
        verbose_name="Background карточек на главной стр", max_length=255, blank=True, null=True,
        help_text="Выбрать один из цветов для фона: srcl1, srcl2, srcl3, srcl4, srcl5"
    )
    tools_used_one = models.CharField(
        max_length=125, verbose_name="Используемый инструмент #1",
        blank=True, help_text="Необязательно для заполнения*"
    )
    tools_used_two = models.CharField(
        max_length=125, verbose_name="Используемый инструмент #2",
        blank=True, help_text="Необязательно для заполнения*"
    )
    tools_used_three = models.CharField(
        max_length=125, verbose_name="Используемый инструмент #3",
        blank=True, help_text="Необязательно для заполнения*"
    )
    tools_used_four = models.CharField(
        max_length=125, verbose_name="Используемый инструмент #4",
        blank=True, help_text="Необязательно для заполнения*"
    )

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def get_absolute_url(self):
        return get_post_url(self, 'post_detail')


class Team(Post):
    skills = models.TextField(verbose_name="Навыки члена команды", blank=True)
    age = models.PositiveIntegerField(verbose_name="Возраст", blank=True)
    telegram = models.CharField(max_length=225, verbose_name="Telegram ссылка", blank=True)
    instagram = models.CharField(max_length=225, verbose_name="Instagram ссылка", blank=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команда"


class Helpbiz(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(verbose_name="Фото")
    backg = models.CharField(
        verbose_name="Background карточек на главной стр", max_length=50,
        help_text="Выбрать один из цветов для фона: cd2, cd3, cd4, cd5, cd6, cd7, cd8, cd9, cd10, cd11"
    )
    speed = models.CharField(
        verbose_name="Скорость выхода поста", max_length=50, blank=True, null=True,
        help_text="Выбрать один из скоростей: 0.2, 0.4, 0.6, 0.8, 1.2, 1.4"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сферы бизнеса"
        verbose_name_plural = "Сферы бизнеса"


class Statistic(models.Model):
    title = models.CharField(max_length=155, verbose_name="Название")
    image = models.ImageField(verbose_name="Фото")
    number = models.PositiveSmallIntegerField(verbose_name="Число (цифра)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блок Нашей Статистики"
        verbose_name_plural = "Блок Нашей Статистики"



