# Generated by Django 4.0.4 on 2022-06-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_employe_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='langue',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='tel',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
