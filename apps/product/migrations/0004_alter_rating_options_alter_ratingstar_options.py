# Generated by Django 5.0 on 2024-01-10 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_ratingstar_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Rating', 'verbose_name_plural': 'RatingЯs'},
        ),
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Star Value', 'verbose_name_plural': 'Star Value'},
        ),
    ]