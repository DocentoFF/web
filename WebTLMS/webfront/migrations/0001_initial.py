# Generated by Django 4.0.4 on 2022-06-01 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QorDelay', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='CourseTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(max_length=100)),
                ('Maker', models.CharField(max_length=50)),
                ('StudProgram', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('G_access_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameProcess', models.CharField(max_length=100)),
                ('IDBot', models.CharField(max_length=100)),
                ('IDChat', models.CharField(max_length=100)),
                ('CourseName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RFS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameProcess', models.CharField(max_length=100)),
                ('IDBot', models.CharField(max_length=100)),
                ('IDChat', models.CharField(max_length=100)),
                ('CourseName', models.CharField(max_length=100)),
                ('QorDelay', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='SP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudProgramName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatusFlag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_flag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChatTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameChat', models.CharField(max_length=100)),
                ('IDChat', models.CharField(max_length=100)),
                ('g_access', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webfront.gaccess')),
            ],
        ),
        migrations.CreateModel(
            name='BotTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameBot', models.CharField(max_length=100)),
                ('IDBot', models.CharField(max_length=100)),
                ('g_access', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webfront.gaccess')),
            ],
        ),
        migrations.CreateModel(
            name='AuthAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('pass_w', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('f_name', models.CharField(max_length=50)),
                ('g_access', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webfront.gaccess')),
            ],
        ),
    ]