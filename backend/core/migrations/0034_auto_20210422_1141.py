# Generated by Django 3.0.7 on 2021-04-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_raffle_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raffle',
            name='one_address_one_vote',
            field=models.BooleanField(verbose_name='weighted chance'),
        ),
    ]
