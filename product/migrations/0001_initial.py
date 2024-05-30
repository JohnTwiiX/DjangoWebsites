# Generated by Django 5.0.6 on 2024-05-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('category', models.CharField(max_length=100)),
                ('status', models.CharField(default='active', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=100)),
                ('material', models.CharField(blank=True, max_length=100)),
                ('color', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]