# Generated by Django 2.2.5 on 2019-09-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]