# Generated by Django 4.0.3 on 2022-03-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0004_alter_srlistofdispatcher_action_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='srlistofdispatcher',
            name='action_taken',
            field=models.CharField(choices=[('Auto', 'Auto'), ('Manual', 'Manual'), ('Deny', 'Deny')], default='--', max_length=10),
        ),
    ]
