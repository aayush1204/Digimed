# Generated by Django 2.2.4 on 2019-10-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191010_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctormodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.CharField(max_length=4)),
                ('password', models.CharField(max_length=31512)),
            ],
        ),
    ]