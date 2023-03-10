# Generated by Django 4.1.6 on 2023-02-26 14:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='balance',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('OTHER', 'Другое'), ('RIFLES', 'Винтовки'), ('MELEE', 'Ближнее'), ('PISTOLS', 'Пистолеты'), ('SNIPERS', 'Снайперские')], default='OTHER', max_length=100, null=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='coast',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=2000, null=True, verbose_name='Описание'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
