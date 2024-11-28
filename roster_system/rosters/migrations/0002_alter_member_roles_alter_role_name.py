# Generated by Django 4.2.6 on 2024-11-28 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='roles',
            field=models.ManyToManyField(to='rosters.role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]