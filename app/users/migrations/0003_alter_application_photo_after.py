# Generated by Django 4.1.2 on 2022-12-16 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_name_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='photo_after',
            field=models.ImageField(null=True, upload_to='photo_after/%Y/%m/%d/', verbose_name='Фотография заявки после'),
        ),
    ]
