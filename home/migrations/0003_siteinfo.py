# Generated by Django 4.2.5 on 2023-09-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=500)),
                ('address2', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('time', models.CharField(max_length=50)),
            ],
        ),
    ]