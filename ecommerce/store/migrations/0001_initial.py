# Generated by Django 4.1.6 on 2023-02-10 01:52

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
                ('name', models.CharField(db_index=True, max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('brand', models.CharField(default='sem-marca', max_length=250)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'produtos',
            },
        ),
    ]
