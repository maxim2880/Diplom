# Generated by Django 4.0.1 on 2023-01-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_alter_goal_description_alter_goal_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='board',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AlterField(
            model_name='boardparticipant',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='boardparticipant',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'К выполнению'), (2, 'В процессе'), (3, 'Выполнено'), (4, 'Архив')], default=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AlterField(
            model_name='goalcategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='goalcategory',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AlterField(
            model_name='goalcomment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='goalcomment',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
    ]
