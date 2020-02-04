# Generated by Django 2.2.9 on 2020-02-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures', '0006_auto_20200203_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=32, verbose_name='Ady: ')),
                ('blog_text', models.TextField(verbose_name='Teksti: ')),
                ('blog_img', models.ImageField(default='default.jpg', upload_to='furnitures/about/', verbose_name='Suraty: ')),
            ],
        ),
        migrations.CreateModel(
            name='AboutDiplom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diplom_txt', models.CharField(max_length=32, verbose_name='Diplom Ady:')),
                ('diplom_img', models.ImageField(default='default.jpg', upload_to='furnitures/about/', verbose_name='Diplom Suraty')),
            ],
        ),
        migrations.CreateModel(
            name='AboutImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_main_image', models.ImageField(default='default.jpg', upload_to='furnitures/about/', verbose_name='Biz Barada Suraty: ')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=32, verbose_name='Kärhananyň Ady: ')),
                ('company_logo', models.ImageField(default='default.jpg', upload_to='furnitures/logo/', verbose_name='Kärhana Logotip: ')),
                ('company_slogan', models.CharField(max_length=128, verbose_name='Kärhananyň Slogany: ')),
            ],
        ),
        migrations.CreateModel(
            name='StoreAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_map_link', models.TextField(verbose_name='Google Karta Link')),
                ('store_img', models.ImageField(default='default.jpg', upload_to='furnitures/stores/', verbose_name='Magazin Suraty')),
                ('address_line1', models.CharField(max_length=64, verbose_name='Address 1 setir : ')),
                ('address_line2', models.CharField(blank=True, max_length=64, verbose_name='Address 2 setir : ')),
                ('phone1', models.CharField(max_length=32, verbose_name='Telefon 1 ')),
                ('phone2', models.CharField(blank=True, max_length=32, verbose_name='Telefon 2 ')),
                ('phone3', models.CharField(blank=True, max_length=32, verbose_name='Telefon 3 ')),
                ('e_mail', models.CharField(blank=True, max_length=32, verbose_name='Email : ')),
            ],
        ),
        migrations.RemoveField(
            model_name='main_page',
            name='about_company',
        ),
        migrations.RemoveField(
            model_name='main_page',
            name='company_name',
        ),
        migrations.AddField(
            model_name='main_page',
            name='about_main',
            field=models.TextField(blank=True, verbose_name='Giňişleýin'),
        ),
        migrations.AddField(
            model_name='main_page',
            name='main_title',
            field=models.CharField(blank=True, max_length=64, verbose_name='Ady'),
        ),
    ]