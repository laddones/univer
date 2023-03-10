# Generated by Django 4.1.7 on 2023-03-04 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_panel', '0007_alter_links_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin_add', to=settings.AUTH_USER_MODEL, verbose_name='Адмін'),
        ),
        migrations.AlterField(
            model_name='links',
            name='link_type',
            field=models.CharField(choices=[('YOUTUBE', 'Youtube'), ('TWITTER', 'Twitter'), ('TELEGRAM', 'Telegram'), ('INSTAGRAM', 'Instagram'), ('FACEBOOK', 'Facebook'), ('TIKTOK', 'TikTok'), ('OTHER', 'Інший тип')], default='OTHER', max_length=10, verbose_name='Статус посилання'),
        ),
    ]
