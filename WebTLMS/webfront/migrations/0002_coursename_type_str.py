# Generated by Django 4.0.4 on 2022-06-02 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webfront', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursename',
            name='type_STR',
            field=models.CharField(max_length=50, null=True),
        ),
    ]