# Generated by Django 2.0.1 on 2018-01-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_project_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='soft_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
