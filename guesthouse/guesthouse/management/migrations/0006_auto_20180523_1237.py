# Generated by Django 2.0.5 on 2018-05-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20180522_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
