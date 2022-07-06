# Generated by Django 4.0.5 on 2022-07-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
