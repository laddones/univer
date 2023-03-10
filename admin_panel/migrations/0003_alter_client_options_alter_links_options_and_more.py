# Generated by Django 4.1.7 on 2023-03-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_links_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-time_update'], 'verbose_name': 'Користувача', 'verbose_name_plural': 'Користувачі'},
        ),
        migrations.AlterModelOptions(
            name='links',
            options={'ordering': ['-time_update'], 'verbose_name': 'Посилання', 'verbose_name_plural': 'Посилання'},
        ),
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.BooleanField(default=False, max_length=10, verbose_name='Підтверджений'),
        ),
    ]
