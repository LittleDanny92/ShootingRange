# Generated by Django 4.2.8 on 2024-08-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookedDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_field', models.DateTimeField()),
                ('instructor_field', models.BooleanField(default=False)),
                ('selected_weapon', models.CharField(max_length=100)),
                ('name_field', models.CharField(max_length=100)),
                ('email_field', models.CharField(max_length=100)),
            ],
        ),
    ]
