# Generated by Django 4.0.6 on 2022-12-30 14:37

import base.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('upload_file', models.FileField(blank=True, upload_to=base.models.get_user_file_folder)),
                ('is_converted', models.BooleanField(default=False)),
                ('uploaded_on', models.DateTimeField(default=datetime.datetime(2022, 12, 30, 14, 37, 41, 906322, tzinfo=utc))),
                ('uploaded_by', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('added_on', models.DurationField()),
                ('added_by', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to=settings.AUTH_USER_MODEL)),
                ('audio', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='audio', to='base.audio')),
            ],
        ),
    ]
