# Generated by Django 4.2.7 on 2023-11-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_merge_0002_item_discount_0004_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
