# Generated by Django 4.2.2 on 2023-07-27 16:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("agents", "0005_alter_agent_config"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="agent",
            name="agent_class_path",
        ),
    ]
