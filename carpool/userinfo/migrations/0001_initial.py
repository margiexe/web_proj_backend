# Generated by Django 5.0.2 on 2024-03-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50)),
                ('p_email', models.EmailField(max_length=254)),
                ('car_name', models.CharField(max_length=50)),
                ('seats_available', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=50)),
                ('r_email', models.EmailField(max_length=254)),
            ],
        ),
    ]