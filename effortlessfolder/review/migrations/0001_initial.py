# Generated by Django 3.2.9 on 2021-12-04 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(error_messages={'unique': '이미 있는 제목입니다.'}, max_length=50, unique=True)),
                ('content', models.TextField(null=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('dt_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
            ],
        ),
    ]
