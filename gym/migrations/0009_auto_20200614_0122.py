# Generated by Django 3.0.6 on 2020-06-14 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0008_auto_20200614_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]