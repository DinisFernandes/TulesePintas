# Generated by Django 3.2.4 on 2021-06-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20210623_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tratado',
            field=models.BooleanField(default=False),
        ),
    ]