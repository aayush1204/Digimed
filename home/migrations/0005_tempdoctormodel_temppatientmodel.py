# Generated by Django 2.2.4 on 2019-10-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20191010_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='tempdoctormodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.CharField(default=0, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='temppatientmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=4)),
            ],
        ),
    ]
