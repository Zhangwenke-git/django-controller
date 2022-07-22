# Generated by Django 3.2.8 on 2022-07-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_remove_database_database_type_9a2b4d_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='database',
            index=models.Index(fields=['type', 'host', 'dbname'], name='database_type_9a2b4d_idx'),
        ),
    ]