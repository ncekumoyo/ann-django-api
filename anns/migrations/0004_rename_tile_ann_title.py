# Generated by Django 4.1.1 on 2023-04-11 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anns', '0003_ann_tile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ann',
            old_name='tile',
            new_name='title',
        ),
    ]
