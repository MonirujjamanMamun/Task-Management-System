# Generated by Django 4.2.7 on 2023-12-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_taskcategorymodel_task'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskmode',
            old_name='task_assign',
            new_name='task_assign_Date',
        ),
        migrations.AddField(
            model_name='taskmode',
            name='category',
            field=models.ManyToManyField(to='category.taskcategorymodel'),
        ),
    ]
