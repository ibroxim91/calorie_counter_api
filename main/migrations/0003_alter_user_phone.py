# Generated by Django 4.2 on 2024-02-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=13, verbose_name='Phone'),
        ),
    ]