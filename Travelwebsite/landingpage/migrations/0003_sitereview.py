# Generated by Django 3.0.4 on 2020-04-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_destination_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
            ],
        ),
    ]
