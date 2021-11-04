# Generated by Django 3.2.8 on 2021-11-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatmap_collections', '0031_alter_comment_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beatmap',
            name='artist',
            field=models.CharField(default='Kenji Ninuma', max_length=1000),
        ),
        migrations.AlterField(
            model_name='beatmap',
            name='creator',
            field=models.CharField(default='peppy', max_length=1000),
        ),
        migrations.AlterField(
            model_name='beatmap',
            name='source',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='beatmap',
            name='title',
            field=models.CharField(default='DISCO PRINCE', max_length=1000),
        ),
    ]
