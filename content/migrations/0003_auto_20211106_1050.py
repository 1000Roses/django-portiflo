# Generated by Django 3.2.9 on 2021-11-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20211106_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
