# Generated by Django 4.0.4 on 2022-05-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_thumbnail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail_image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
