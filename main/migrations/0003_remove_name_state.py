# Generated by Django 2.0.3 on 2018-03-25 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_nameinstate_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='state',
        ),
    ]
