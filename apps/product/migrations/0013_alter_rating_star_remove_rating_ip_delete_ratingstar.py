# Generated by Django 5.0 on 2024-01-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_reviews_email_remove_reviews_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.IntegerField(),
        ),
        migrations.RemoveField(
            model_name='rating',
            name='ip',
        ),
        migrations.DeleteModel(
            name='RatingStar',
        ),
    ]
