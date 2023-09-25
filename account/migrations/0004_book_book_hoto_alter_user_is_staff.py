# Generated by Django 4.0.6 on 2022-07-06 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_book_available_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_hoto',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
