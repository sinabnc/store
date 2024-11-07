# Generated by Django 5.1.1 on 2024-10-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subname', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='offer_images/')),
                ('image1', models.ImageField(upload_to='offer_images/')),
                ('price', models.IntegerField()),
                ('gram', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offer',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subname', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('image1', models.ImageField(upload_to='blog_images/')),
                ('price', models.IntegerField()),
                ('gram', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
