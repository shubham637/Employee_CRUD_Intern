# Generated by Django 3.2 on 2024-08-28 11:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={},
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='created_at',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='updated_at',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='date_of_birth',
            new_name='start_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
