# Generated by Django 4.2.7 on 2023-12-01 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_merge_20231127_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineitem',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
