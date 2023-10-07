# Generated by Django 4.2.6 on 2023-10-06 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_rename_user_department_doctor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='doctor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department', to=settings.AUTH_USER_MODEL),
        ),
    ]
