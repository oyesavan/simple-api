# Generated by Django 3.1.5 on 2021-01-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_villain'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Villain',
        ),
        migrations.AddField(
            model_name='hero',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=10),
        ),
    ]
