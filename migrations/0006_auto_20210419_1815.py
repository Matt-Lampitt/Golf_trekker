# Generated by Django 3.2 on 2021-04-19 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golftrekker', '0005_auto_20210417_0158'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Instructor',
        ),
        migrations.RemoveField(
            model_name='instruction',
            name='instruction',
        ),
        migrations.AddField(
            model_name='instruction',
            name='instructor',
            field=models.CharField(default='Coach', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instruction',
            name='instructor_topic',
            field=models.CharField(default='Subject', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instruction',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
