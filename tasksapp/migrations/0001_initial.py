# Generated by Django 5.0.4 on 2024-05-04 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=64)),
                ('area', models.FloatField()),
                ('number_of_rooms', models.IntegerField()),
                ('parking', models.BooleanField(default=False)),
                ('pets', models.BooleanField(default=False)),
                ('toilets', models.BooleanField(default=False)),
                ('bathroom', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='house_images')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tasksapp.house')),
            ],
        ),
    ]
