# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 02:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidade', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LancamentosContabil',
            new_name='LancamentoContabil',
        ),
        migrations.RenameModel(
            old_name='SaldosContabeis',
            new_name='SaldoContabil',
        ),
    ]
