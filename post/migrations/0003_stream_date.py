# Generated by Django 3.1.3 on 2020-11-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20201118_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='date',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
    ]
