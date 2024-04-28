# Generated by Django 5.0.3 on 2024-04-24 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_url', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=50)),
                ('imdb_score', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Film',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
