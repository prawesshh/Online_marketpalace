# Generated by Django 2.2.4 on 2019-09-18 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='proimage',
            new_name='image',
        ),
    ]
