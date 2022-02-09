# Generated by Django 4.0 on 2022-02-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_interest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=127, null=True)),
                ('description', models.CharField(blank=True, max_length=127, null=True)),
                ('year', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
            },
        ),
    ]
