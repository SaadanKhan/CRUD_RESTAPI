# Generated by Django 4.2 on 2023-04-16 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cados_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comapny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]