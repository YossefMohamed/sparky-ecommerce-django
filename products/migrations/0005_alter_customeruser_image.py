# Generated by Django 4.0.4 on 2022-05-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_customeruser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='image',
            field=models.ImageField(blank=True, default='/images/avatar.png', null=True, upload_to='images/user/%d'),
        ),
    ]
