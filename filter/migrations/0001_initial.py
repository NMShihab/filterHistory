# Generated by Django 3.2.6 on 2021-09-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('user', models.CharField(max_length=100)),
                ('keyWord', models.CharField(max_length=10)),
                ('searchedDate', models.DateTimeField()),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
