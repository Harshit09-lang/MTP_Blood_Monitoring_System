# Generated by Django 4.0.4 on 2023-10-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(upload_to='data_file')),
            ],
        ),
        migrations.CreateModel(
            name='MLmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ml_file', models.FileField(upload_to='ml_model')),
            ],
        ),
    ]
