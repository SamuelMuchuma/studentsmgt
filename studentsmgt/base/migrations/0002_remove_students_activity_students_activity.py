# Generated by Django 4.1 on 2022-08-22 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='activity',
        ),
        migrations.AddField(
            model_name='students',
            name='activity',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, related_name='activities', to='base.school_activities'),
            preserve_default=False,
        ),
    ]
