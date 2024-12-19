# Generated by Django 5.1.4 on 2024-12-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Haзвание')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Onисание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Из0бражение')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Leнa')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Leнa')),
            ],
            options={
                'verbose_name': 'Продукты',
                'verbose_name_plural': 'продукт',
                'db_table': 'product',
            },
        ),
    ]
