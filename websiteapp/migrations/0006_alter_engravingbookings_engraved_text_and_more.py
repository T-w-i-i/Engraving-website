# Generated by Django 4.1.7 on 2023-03-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0005_engravingbookings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engravingbookings',
            name='Engraved_text',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='engravingbookings',
            name='font_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
