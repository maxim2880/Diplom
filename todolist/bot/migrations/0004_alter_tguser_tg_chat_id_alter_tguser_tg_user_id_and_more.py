# Generated by Django 4.0.1 on 2023-01-03 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bot', '0003_alter_tguser_tg_chat_id_alter_tguser_tg_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='tg_chat_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='tg_user_id',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='verification_code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
