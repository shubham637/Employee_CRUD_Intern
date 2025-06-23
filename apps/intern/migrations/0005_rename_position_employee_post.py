

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0004_auto_20240829_0528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='position',
            new_name='post',
        ),
    ]
