# Generated by Django 4.0.3 on 2022-06-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkpage', '0002_alter_link_description_alter_link_link_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]