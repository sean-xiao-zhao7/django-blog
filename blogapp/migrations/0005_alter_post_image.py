# Generated by Django 3.2.7 on 2021-09-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
