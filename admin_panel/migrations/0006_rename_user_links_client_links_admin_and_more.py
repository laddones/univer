# Generated by Django 4.1.7 on 2023-03-03 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_panel', '0005_alter_links_link_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='user',
            new_name='client',
        ),
        migrations.AddField(
            model_name='links',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin_add', to=settings.AUTH_USER_MODEL, verbose_name='Адмін'),
        ),
        migrations.CreateModel(
            name='LinkClientStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_status', models.CharField(choices=[('REPORTED', 'Reported'), ('SKIPPED', 'Skipped'), ('DELETED', 'Deleted'), ('PROCESSING', 'Processing')], default='PROCESSING', max_length=20, verbose_name='Статус')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Час створення')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Час оновлення')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_telegram', to='admin_panel.client', verbose_name='User Telegram')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_link', to='admin_panel.links', verbose_name='Link')),
            ],
        ),
    ]
