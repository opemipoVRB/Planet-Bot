# Generated by Django 2.1.2 on 2018-10-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottieverse', '0002_chatlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botresponse',
            name='response',
            field=models.CharField(default='No message', max_length=255),
        ),
    ]