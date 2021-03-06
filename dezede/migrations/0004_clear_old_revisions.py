# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 05:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dezede', '0003_add_unaccent'),
    ]
    run_before = [
        ('reversion', '0003_auto_20160601_1600'),
    ]

    operations = [
        migrations.RunSQL("""
        DELETE FROM reversion_version WHERE id IN (
            SELECT id FROM (
                SELECT
                    version.id,
                    version.revision_id,
                    COUNT(*) OVER (PARTITION BY content_type_id, object_id
                                   ORDER BY date_created DESC) AS n
                FROM reversion_version AS version
                INNER JOIN reversion_revision AS revision
                    ON revision.id = version.revision_id
            ) AS version
            WHERE n > 1
                  OR revision_id IS NULL
        );
        """),
        migrations.RunSQL("""
        DELETE FROM reversion_revision WHERE NOT EXISTS (
            SELECT * FROM reversion_version
            WHERE revision_id = reversion_revision.id
        );
        """),
    ]
