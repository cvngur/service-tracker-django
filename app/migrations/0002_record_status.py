# Generated by Django 3.0.6 on 2020-05-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='status',
            field=models.CharField(default='Application received', max_length=255),
            preserve_default=False,
        ),
    ]