# Generated by Django 2.2.6 on 2019-10-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForumArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('author', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ForumArticle',
                'verbose_name_plural': 'ForumArticles',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
