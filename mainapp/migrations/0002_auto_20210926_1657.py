# Generated by Django 3.2.7 on 2021-09-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todotext',
            options={'verbose_name': 'Todotext', 'verbose_name_plural': 'Todotexts'},
        ),
        migrations.AddField(
            model_name='todotext',
            name='created',
            field=models.DateField(default='2021-09-26'),
        ),
    ]
