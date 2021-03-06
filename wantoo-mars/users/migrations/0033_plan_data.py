# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 19:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def load_plans(apps, schema_editor):
    Plan = apps.get_model("users", "Plan")
    plan_free = Plan(id=4, name="STARTER", plan_type="starter_monthly", interval="monthly", amount=7, currency="USD",
                     description="Starter plan", trial_period_days=30)
    plan_free.save()
    plan_pro = Plan(id=5, name="PRO", plan_type="pro_25_monthly", interval="monthly", amount=25, currency="USD",
                    description="Pro plan", trial_period_days=30)
    plan_pro.save()


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0032_memberinvitation'),
    ]

    operations = [
        migrations.RunPython(load_plans),
    ]
