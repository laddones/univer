# Generated by Django 4.1.7 on 2023-03-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_id', models.BigIntegerField(db_index=True, primary_key=True, serialize=False, unique=True, verbose_name='User Id')),
                ('status', models.BooleanField(blank=True, default=False, max_length=10, null=True, verbose_name='Підтверджений')),
                ('username', models.CharField(blank=True, max_length=64, null=True, verbose_name='Логин')),
                ('first_name', models.CharField(blank=True, max_length=64, null=True, verbose_name="Ім'я")),
                ('last_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Призвище')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телелефону')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Електронна пошта')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Час створення')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Час оновлення')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255, unique=True, verbose_name='Посилання')),
                ('description', models.TextField(verbose_name='Опис ресурсу')),
                ('link_status', models.CharField(choices=[('DELETED', 'Видалений'), ('PUBLISHED', 'Опублікований'), ('PROCESSING', 'В обробці'), ('BLOCKED', 'Заблокований')], default='PROCESSING', max_length=10, verbose_name='Статус посилання')),
                ('link_type', models.CharField(choices=[('YOUTUBE', 'Youtube'), ('TWITTER', 'Twitter'), ('TELEGRAM', 'Telegram'), ('INSTAGRAM', 'Instagram'), ('FACEBOOK', 'Facebook'), ('TIKTOK', 'TikTok'), ('VIBER', 'Viber'), ('OTHER', 'Другой тип')], default='OTHER', max_length=10, verbose_name='Статус посилання')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Час створення')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Час оновлення')),
            ],
        ),
    ]
