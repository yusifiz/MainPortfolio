# Generated by Django 4.0 on 2022-02-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='blog/')),
            ],
        ),
    ]
