# Generated by Django 3.2 on 2023-02-16 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='company/')),
                ('subtitle', models.CharField(max_length=500)),
                ('fb_link', models.URLField(blank=True, null=True)),
                ('tw_link', models.URLField(blank=True, null=True)),
                ('in_link', models.URLField(blank=True, null=True)),
                ('LI_link', models.URLField(blank=True, null=True)),
                ('address', models.TextField(max_length=200)),
                ('phone_number', models.TextField(max_length=200)),
                ('email', models.TextField(max_length=200)),
                ('call_us', models.CharField(max_length=25)),
                ('email_us', models.EmailField(max_length=25)),
            ],
        ),
    ]
