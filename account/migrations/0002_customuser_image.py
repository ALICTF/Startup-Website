# Generated by Django 5.1 on 2024-08-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='', upload_to='cover/profile/'),
            preserve_default=False,
        ),
    ]