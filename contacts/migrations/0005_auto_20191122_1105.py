# Generated by Django 2.2.6 on 2019-11-22 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_real_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='real_author',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
