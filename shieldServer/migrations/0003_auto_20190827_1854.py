# Generated by Django 2.2.4 on 2019-08-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shieldServer', '0002_borrower'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_phone',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='user_rank',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='user_real_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
