# Generated by Django 4.0.1 on 2022-02-28 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0005_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sellers.sellers'),
        ),
    ]