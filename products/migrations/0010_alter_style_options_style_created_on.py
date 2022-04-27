# Generated by Django 4.0.3 on 2022-04-27 10:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_accessories_task_status_processes_task_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='style',
            options={'ordering': ['-created_on'], 'verbose_name': 'Style', 'verbose_name_plural': 'Styles'},
        ),
        migrations.AddField(
            model_name='style',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]