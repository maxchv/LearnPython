# Generated by Django 4.0.4 on 2022-05-15 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_comment_created_alter_post_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]