# Generated by Django 4.2.3 on 2023-09-18 14:56

import clubs.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=clubs.models.getFilename)),
                ('incharge_name', models.CharField(max_length=50)),
                ('organizer_name', models.CharField(max_length=50)),
                ('boys_name', models.CharField(max_length=50)),
                ('girls_name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=500, null=True)),
                ('event_organizer', models.CharField(blank=True, max_length=50, null=True)),
                ('event_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Index_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texts', models.TextField(blank=True, max_length=2000, null=True)),
                ('imaages', models.ImageField(blank=True, null=True, upload_to=clubs.models.getFilename)),
            ],
        ),
        migrations.CreateModel(
            name='Club_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '1234567890'.", regex='^\\d{9,10}$')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.club')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.department')),
            ],
        ),
    ]
