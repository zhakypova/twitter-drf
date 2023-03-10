# Generated by Django 3.2 on 2022-12-26 14:23

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
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Twit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwitLikeDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_dislike', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('twit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.twit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentLikeDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_dislike', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='twit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.twit'),
        ),
    ]
