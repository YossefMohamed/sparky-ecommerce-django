# Generated by Django 4.0.4 on 2022-05-29 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_image1_customeruser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='image',
            field=models.ImageField(blank=True, default='https://www.blexar.com/avatar.png', null=True, upload_to='images/user/%d'),
        ),
    ]
