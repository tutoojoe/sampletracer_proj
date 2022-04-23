# Generated by Django 4.0.3 on 2022-04-23 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0005_alter_user_email_alter_user_user_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MANAGER',
        ),
        migrations.CreateModel(
            name='Merchandiser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('useraccounts.user',),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('NEWUSER', 'NewUser'), ('MERCHANDISER', 'Merchandiser'), ('CUSTOMER', 'Customer'), ('JUNIOREMP', 'JuniorEmp'), ('STOREKEEPER', 'Storekeeper')], default='NEWUSER', help_text='User type/role - to be selected from the given list. This will determine the permissions. \nDefault value will be NEWUSER on registration.', max_length=50, verbose_name='Type of user'),
        ),
    ]
