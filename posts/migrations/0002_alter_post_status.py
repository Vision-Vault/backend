# Generated by Django 4.1.5 on 2023-08-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('active', 'incomplete'), ('Draft', 'complete')], default='under_donation', max_length=20),
        ),
    ]