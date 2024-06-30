# Generated by Django 5.0.3 on 2024-06-23 17:24

import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('wowsite', '0011_wowclass_tags'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['pk'], 'verbose_name': 'Ролі', 'verbose_name_plural': 'Ролі'},
        ),
        migrations.AlterModelOptions(
            name='specialization',
            options={'verbose_name': 'Спеціалізації', 'verbose_name_plural': 'Спеціалізації'},
        ),
        migrations.AlterModelOptions(
            name='wowclass',
            options={'ordering': ['created'], 'verbose_name': 'Класси', 'verbose_name_plural': 'Класси'},
        ),
        migrations.AlterModelManagers(
            name='wowclass',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='role',
            name='title',
            field=models.CharField(db_index=True, max_length=10, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='role', to='wowsite.role', verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='wow_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wow_class', to='wowsite.wowclass', verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='Виконано?'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач'),
        ),
        migrations.AlterField(
            model_name='wowclass',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='wowclass',
            name='description',
            field=models.TextField(blank=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='wowclass',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Чорновик'), (True, 'Published')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='wowclass',
            name='roles',
            field=models.ManyToManyField(related_name='roles', to='wowsite.role', verbose_name='Ролі'),
        ),
        migrations.AlterField(
            model_name='wowclass',
            name='slug',
            field=models.SlugField(max_length=20, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='wowclass',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='wowclass',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='wowclass',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата оновлення'),
        ),
        migrations.AddIndex(
            model_name='role',
            index=models.Index(fields=['slug'], name='wowsite_rol_slug_5d5d36_idx'),
        ),
    ]