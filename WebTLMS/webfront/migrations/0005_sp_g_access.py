# Generated by Django 4.0.4 on 2022-06-02 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webfront', '0004_typestr'),
    ]

    operations = [
        migrations.AddField(
            model_name='sp',
            name='g_access',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webfront.gaccess'),
        ),
    ]
