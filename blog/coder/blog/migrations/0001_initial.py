# Generated by Django 3.0.6 on 2020-05-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]