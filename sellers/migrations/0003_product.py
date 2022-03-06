# Generated by Django 4.0.1 on 2022-02-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0002_sellers_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.TextField(max_length=300)),
                ('price', models.TextField()),
                ('quantity', models.TextField()),
                ('description', models.TextField(max_length=500)),
                ('med_img', models.ImageField(upload_to='')),
            ],
        ),
    ]