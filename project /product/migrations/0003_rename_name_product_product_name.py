# Generated by Django 5.0.4 on 2024-05-02 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]
