# Generated by Django 4.2.10 on 2024-03-12 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shiki', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anime', to='shiki.genre', verbose_name='Жанр'),
        ),
    ]
