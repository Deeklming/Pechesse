# Generated by Django 4.2.4 on 2023-08-27 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]