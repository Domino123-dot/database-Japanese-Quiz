# Generated by Django 4.0.2 on 2023-02-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_remove_questions_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='max_points_to_get',
            field=models.IntegerField(default=0, verbose_name='max_points_to_get'),
        ),
    ]
