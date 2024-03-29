# Generated by Django 2.2.3 on 2019-07-12 12:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190711_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('start', models.DateField(default=django.utils.timezone.now)),
                ('end', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Четверть',
                'verbose_name_plural': 'Четверті',
            },
        ),
    ]
