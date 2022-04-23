# Generated by Django 4.0.3 on 2022-04-23 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0006_delete_manager_merchandiser_alter_user_user_type'),
        ('products', '0003_style_customer_alter_style_merchandiser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='merchandiser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccounts.merchandiser', verbose_name='Merchandiser name'),
        ),
    ]