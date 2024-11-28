# Generated by Django 4.2.6 on 2024-11-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sunday_date', models.DateField()),
                ('members', models.ManyToManyField(related_name='rosters', to='rosters.member')),
                ('roles', models.ManyToManyField(related_name='rosters', to='rosters.role')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='roles',
            field=models.ManyToManyField(related_name='members', to='rosters.role'),
        ),
    ]