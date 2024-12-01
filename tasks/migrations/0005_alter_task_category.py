# Generated by Django 5.1.2 on 2024-11-14 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_remove_task_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('home', 'Home'), ('casadepaz', 'Casa de Paz'), ('discipulado', 'Discipulado'), ('aviva2', 'Aviva2'), ('avivakids', 'Avivakids'), ('jovenes', 'Jovenes')], default='', max_length=20),
        ),
    ]