# Generated by Django 3.2.12 on 2022-03-23 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='demo.category'),
            preserve_default=False,
        ),
    ]