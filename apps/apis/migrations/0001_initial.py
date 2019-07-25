# Generated by Django 2.2.3 on 2019-07-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.CharField(db_column='alg_id', max_length=255, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('path', models.CharField(max_length=255)),
                ('class_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'algorithm',
            },
        ),
    ]