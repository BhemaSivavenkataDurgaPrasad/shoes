# Generated by Django 4.1.7 on 2023-03-31 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=125)),
                ('size', models.IntegerField(default=6)),
                ('price', models.IntegerField(default=250)),
            ],
        ),
    ]
