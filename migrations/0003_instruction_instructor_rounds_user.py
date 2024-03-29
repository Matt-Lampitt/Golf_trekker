# Generated by Django 3.2 on 2021-04-15 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('golftrekker', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.CharField(choices=[('PT', 'Putting'), ('CP', 'Chipping'), ('PH', 'Pitching'), ('FS', 'Full Swing')], default='PT', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.CharField(choices=[('EC', 'Eric Cogorno'), ('SC', 'Shawn Clement')], default='EC', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rounds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_played', models.DateField()),
                ('course_name', models.CharField(max_length=255)),
                ('course_location', models.CharField(max_length=255)),
                ('course_par', models.IntegerField(max_length=2)),
                ('course_score', models.IntegerField(max_length=3)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('password', models.CharField(max_length=255)),
                ('password_confirm', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
