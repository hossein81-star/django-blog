# Generated by Django 5.2.4 on 2025-07-23 16:15

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('slug', models.CharField(max_length=250)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('cul', 'Culture'), ('biz', 'Business'), ('lif', 'Lifestyle'), ('tec', 'Technology')], default='cul')),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published'), ('RJ', 'Rejected')], default='DF', max_length=2)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('publish', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auther', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish'],
                'indexes': [models.Index(fields=['-publish'], name='blog_post_publish_bb7600_idx')],
            },
        ),
    ]
