# Generated by Django 3.0.5 on 2021-02-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210204_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoapp_fields',
            name='taskID',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todoapp_fields',
            name='activity',
            field=models.TextField(),
        ),
    ]
