# Generated by Django 3.2.4 on 2021-09-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mail", "0008_auto_20210830_2352"),
    ]

    operations = [
        migrations.AddField(
            model_name="queuedmail",
            name="locale",
            field=models.CharField(max_length=5, null=True),
        ),
    ]
