# Generated by Django 4.0.2 on 2022-04-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfa_implmentation', '0004_user3mfacodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user3mfacodes',
            name='potp',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='pnumber',
            field=models.CharField(default=123456, max_length=10),
            preserve_default=False,
        ),
    ]