# Generated by Django 3.2 on 2021-04-15 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golftrekker', '0003_instruction_instructor_rounds_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rounds',
            name='course_par',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rounds',
            name='course_score',
            field=models.IntegerField(),
        ),
    ]
