# Generated by Django 4.0.1 on 2022-01-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.TextField(max_length=50)),
                ('seller_email', models.EmailField(max_length=254, unique=True)),
                ('seller_password', models.TextField()),
            ],
        ),
    ]
