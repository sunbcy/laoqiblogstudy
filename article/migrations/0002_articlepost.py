# Generated by Django 2.2.6 on 2019-11-13 02:26

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=500)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2019, 11, 13, 2, 26, 51, 958489, tzinfo=utc))),
                ('updated', models.DateTimeField(default=datetime.datetime(2019, 11, 13, 2, 26, 51, 958489, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=None, related_name='article', to=settings.AUTH_USER_MODEL)),
                ('column', models.ForeignKey(on_delete=None, related_name='article_column', to='article.ArticleColumn')),
            ],
            options={
                'ordering': ('title',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]