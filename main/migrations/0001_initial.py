# Generated by Django 4.0.3 on 2022-03-29 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ТИП')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('cost', models.FloatField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cost_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.costtype')),
            ],
        ),
    ]
