# Generated by Django 4.0.4 on 2022-06-02 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webfront', '0007_coursetable_coursefolder'),
    ]

    operations = [
        migrations.AddField(
            model_name='llog',
            name='StatusFlag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webfront.statusflag'),
        ),
        migrations.AlterField(
            model_name='llog',
            name='CourseName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webfront.coursename'),
        ),
        migrations.AlterField(
            model_name='llog',
            name='IDBot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webfront.bottable'),
        ),
        migrations.AlterField(
            model_name='llog',
            name='IDChat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webfront.chattable'),
        ),
    ]
