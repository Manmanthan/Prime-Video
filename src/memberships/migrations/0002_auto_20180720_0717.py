# Generated by Django 2.0.7 on 2018-07-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Enterprise', 'ent'), ('Professional', 'pro'), ('Free', 'free')], default='Free', max_length=30),
        ),
    ]
