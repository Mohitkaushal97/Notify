# Generated by Django 3.1.2 on 2020-10-05 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=8)),
                ('lat', models.CharField(max_length=8)),
                ('long', models.CharField(max_length=8)),
                ('title', models.CharField(default='', max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('device_token', models.CharField(max_length=8)),
            ],
        ),
    ]
