# Generated by Django 3.1.5 on 2021-01-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20210107_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='alias',
            field=models.CharField(max_length=600),
        ),
    ]