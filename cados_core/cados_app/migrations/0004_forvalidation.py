# Generated by Django 4.2 on 2023-04-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cados_app', '0003_advocate_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForValidation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]