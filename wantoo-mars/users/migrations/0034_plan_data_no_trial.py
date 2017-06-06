# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 19:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def load_plans(apps, schema_editor):
    Plan = apps.get_model("users", "Plan")
    plan_free1 = Plan(id=6, name="STARTER", plan_type="starter_monthly_without_trial", interval="monthly", amount=7,
                     currency="USD",
                     description="Starter plan", trial_period_days=0)
    plan_free1.save()
    plan_pro1 = Plan(id=7, name="PRO", plan_type="pro_25_monthly_without_trial", interval="monthly", amount=25,
                    currency="USD",
                    description="Pro plan", trial_period_days=0)
    plan_pro1.save()


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0032_memberinvitation'),
    ]

    operations = [
        migrations.RunPython(load_plans),
    ]