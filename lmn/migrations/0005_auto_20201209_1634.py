# Generated by Django 3.1.2 on 2020-12-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0004_merge_20201209_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='notes',
        ),
        migrations.AlterField(
            model_name='note',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]