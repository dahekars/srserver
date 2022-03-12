# Generated by Django 4.0.3 on 2022-03-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0002_delete_dispatch_name_delete_srdatabase'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='srlistofdispatcher',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterField(
            model_name='srlistofdispatcher',
            name='action_taken',
            field=models.CharField(choices=[('Auto', 'Auto'), ('Manual', 'Manual'), ('Deny', 'Deny')], default='auto', max_length=10),
        ),
    ]