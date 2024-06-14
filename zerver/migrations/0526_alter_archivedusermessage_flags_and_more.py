# Generated by Django 5.0.6 on 2024-06-14 12:10

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0525_archivedmessage_silent_mode_message_silent_mode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="archivedusermessage",
            name="flags",
            field=bitfield.models.BitField(
                [
                    "read",
                    "starred",
                    "collapsed",
                    "mentioned",
                    "stream_wildcard_mentioned",
                    "topic_wildcard_mentioned",
                    "group_mentioned",
                    "force_expand",
                    "force_collapse",
                    "has_alert_word",
                    "historical",
                    "is_private",
                    "active_mobile_push_notification",
                    "silent_mode",
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="usermessage",
            name="flags",
            field=bitfield.models.BitField(
                [
                    "read",
                    "starred",
                    "collapsed",
                    "mentioned",
                    "stream_wildcard_mentioned",
                    "topic_wildcard_mentioned",
                    "group_mentioned",
                    "force_expand",
                    "force_collapse",
                    "has_alert_word",
                    "historical",
                    "is_private",
                    "active_mobile_push_notification",
                    "silent_mode",
                ],
                default=0,
            ),
        ),
    ]