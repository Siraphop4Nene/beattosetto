# Generated by Django 3.2.8 on 2021-10-20 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beatmap_collections', '0007_alter_ratinglog_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beatmap',
            name='collection',
        ),
        migrations.AddField(
            model_name='beatmap',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='beatmap_collections.collection'),
        ),
    ]
