# Generated by Django 3.0.3 on 2020-05-28 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=4096)),
                ('source', models.URLField()),
                ('published', models.DateTimeField(auto_now=True)),
                ('img', models.FileField(upload_to='upload/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Forex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=4096)),
                ('source', models.URLField()),
                ('published', models.DateTimeField(auto_now=True)),
                ('img', models.FileField(upload_to='upload/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=4096)),
                ('source', models.URLField()),
                ('published', models.DateTimeField(auto_now=True)),
                ('img', models.FileField(upload_to='upload/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=4096)),
                ('source', models.URLField()),
                ('published', models.DateTimeField(auto_now=True)),
                ('img', models.FileField(upload_to='upload/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category')),
            ],
        ),
    ]
