# Generated by Django 4.1.2 on 2022-11-01 07:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rename_id_history_qid'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='transaction_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
