# Generated by Django 4.2.2 on 2023-06-20 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_alter_local_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
