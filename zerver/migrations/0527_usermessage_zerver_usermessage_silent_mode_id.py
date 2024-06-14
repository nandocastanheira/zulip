# Generated by Django 5.0.6 on 2024-06-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0526_alter_archivedusermessage_flags_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="usermessage",
            index=models.Index(
                models.F("user_profile"),
                models.F("message"),
                condition=models.Q(("flags__andnz", 8192)),
                name="zerver_usermessage_silent_mode_id",
            ),
        ),
    ]