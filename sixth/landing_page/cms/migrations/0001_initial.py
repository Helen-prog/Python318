# Generated by Django 5.0.6 on 2024-09-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cms_img', models.ImageField(upload_to='slider_img/', verbose_name='Изображение')),
                ('cms_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('cms_text', models.CharField(max_length=200, verbose_name='Текст')),
                ('cms_css', models.CharField(default='-', max_length=50, verbose_name='CSS класс')),
            ],
            options={
                'verbose_name': 'слайд',
                'verbose_name_plural': 'слайды',
            },
        ),
    ]
