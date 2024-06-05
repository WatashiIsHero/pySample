# Generated by Django 5.0.6 on 2024-05-26 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tw_date', models.CharField()),
                ('tw_time', models.CharField()),
                ('content', models.CharField()),
                ('usr_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tweet.user')),
            ],
        ),
    ]
