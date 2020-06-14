# Generated by Django 3.0.6 on 2020-06-14 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='surname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.DeleteModel(
            name='User_Account',
        ),
    ]