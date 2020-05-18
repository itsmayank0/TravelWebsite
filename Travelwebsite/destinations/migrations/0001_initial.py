# Generated by Django 3.0.4 on 2020-05-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destionations',
            fields=[
                ('title', models.CharField(max_length=2000, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('destionation_image', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('feature1', models.TextField()),
                ('feature2', models.TextField()),
                ('feature3', models.TextField()),
                ('feature4', models.TextField()),
            ],
        ),
    ]