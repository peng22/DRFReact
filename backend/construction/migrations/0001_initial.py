# Generated by Django 3.2.7 on 2021-10-21 10:26

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('name', models.CharField(max_length=255)),
                ('area', models.IntegerField()),
                ('num_of_required_col', models.IntegerField()),
                ('num_of_finished_col', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Water_Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('nuumber_of_cars', models.IntegerField()),
                ('construction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water_supplies', to='construction.construction')),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('section', models.CharField(max_length=255)),
                ('years_of_experience', models.IntegerField()),
                ('age', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cement_Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('weight', models.IntegerField()),
                ('construction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cement_supplies', to='construction.construction')),
            ],
        ),
        migrations.CreateModel(
            name='Brick_Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('nuumber_of_cars', models.IntegerField()),
                ('construction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brick_supplies', to='construction.construction')),
            ],
        ),
    ]
