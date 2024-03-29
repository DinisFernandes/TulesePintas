# Generated by Django 3.2.4 on 2021-06-09 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210609_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='GaleriaPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galeria', models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Galeria')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.post')),
            ],
        ),
    ]
