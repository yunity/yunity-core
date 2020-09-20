# Generated by Django 3.0.9 on 2020-08-16 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('activities', '0023_create_and_set_activity_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='typus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='activities.ActivityType'),
        ),
        migrations.AlterField(
            model_name='activityseries',
            name='typus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_series', to='activities.ActivityType'),
        ),
    ]
