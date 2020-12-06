# Generated by Django 3.1.3 on 2020-12-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True)),
                ('posted_in', models.ManyToManyField(related_name='posted_in', to='posts.Post')),
            ],
        ),
    ]
