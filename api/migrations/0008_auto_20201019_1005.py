# Generated by Django 3.1.2 on 2020-10-19 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_classroom_class_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
