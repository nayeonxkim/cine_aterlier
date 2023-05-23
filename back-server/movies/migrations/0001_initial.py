# Generated by Django 3.2.18 on 2023-05-23 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KarloImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id1', models.IntegerField()),
                ('movie_id2', models.IntegerField()),
                ('original_title1', models.CharField(max_length=255)),
                ('original_title2', models.CharField(max_length=255)),
                ('painter', models.CharField(max_length=255)),
                ('img_url', models.ImageField(upload_to='karloResults/')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('keyword_id', models.IntegerField(primary_key=True, serialize=False)),
                ('keyword_name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('tmdb_id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_language', models.CharField(max_length=255)),
                ('original_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('release_date', models.DateField(null=True)),
                ('poster_path', models.TextField(null=True)),
                ('genre_id', models.IntegerField()),
                ('adult', models.BooleanField(default=False)),
                ('popularity', models.DecimalField(decimal_places=3, default=None, max_digits=20)),
                ('vote_average', models.DecimalField(decimal_places=1, max_digits=20)),
                ('vote_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.keyword')),
                ('tmdb_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.AddField(
            model_name='keyword',
            name='movies',
            field=models.ManyToManyField(related_name='keywords', through='movies.MovieKeyword', to='movies.Movie'),
        ),
    ]
