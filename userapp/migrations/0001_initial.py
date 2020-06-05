# Generated by Django 3.0.5 on 2020-06-04 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=20)),
                ('tz', models.DateTimeField()),
                ('activity_period', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.ActivityPeriod')),
            ],
        ),
    ]
