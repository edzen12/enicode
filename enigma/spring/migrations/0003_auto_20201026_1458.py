# Generated by Django 3.1.2 on 2020-10-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spring', '0002_auto_20201026_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='back_fon',
            field=models.CharField(blank=True, help_text='Выбрать один из цветов для фона: srcl1, srcl2, srcl3, srcl4, srcl5', max_length=255, null=True, verbose_name='Background карточек на главной стр'),
        ),
        migrations.AlterField(
            model_name='service',
            name='backg',
            field=models.CharField(blank=True, help_text='Выбрать один из цветов для фона: a, b, c, d, e, f', max_length=255, null=True, verbose_name='Background слайдера на главной стр'),
        ),
        migrations.AlterField(
            model_name='service',
            name='tools_used_four',
            field=models.CharField(blank=True, help_text='Необязательно для заполнения*', max_length=125, verbose_name='Используемый инструмент #4'),
        ),
        migrations.AlterField(
            model_name='service',
            name='tools_used_one',
            field=models.CharField(blank=True, help_text='Необязательно для заполнения*', max_length=125, verbose_name='Используемый инструмент #1'),
        ),
        migrations.AlterField(
            model_name='service',
            name='tools_used_three',
            field=models.CharField(blank=True, help_text='Необязательно для заполнения*', max_length=125, verbose_name='Используемый инструмент #3'),
        ),
        migrations.AlterField(
            model_name='service',
            name='tools_used_two',
            field=models.CharField(blank=True, help_text='Необязательно для заполнения*', max_length=125, verbose_name='Используемый инструмент #2'),
        ),
    ]
