# Generated by Django 4.1.1 on 2023-04-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entity',
            options={'verbose_name_plural': 'Entities'},
        ),
        migrations.AddField(
            model_name='entity',
            name='short_name',
            field=models.CharField(default='org', max_length=10),
            preserve_default=False,
        ),
    ]
