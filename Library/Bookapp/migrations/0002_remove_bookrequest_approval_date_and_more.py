# Generated by Django 5.0.3 on 2024-05-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookrequest',
            name='approval_date',
        ),
        migrations.RemoveField(
            model_name='bookrequest',
            name='renewal_date',
        ),
        migrations.RemoveField(
            model_name='bookrequest',
            name='return_date',
        ),
        migrations.RemoveField(
            model_name='bookrequest',
            name='return_status',
        ),
        migrations.RemoveField(
            model_name='bookrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
