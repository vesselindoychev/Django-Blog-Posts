# Generated by Django 3.2.19 on 2023-06-19 12:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(5)])),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.country')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
