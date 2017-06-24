# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 02:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LancamentosContabil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_competencia', models.DateField()),
                ('data_lancamento', models.DateField(auto_now=True)),
                ('numero_documento', models.CharField(max_length=12)),
                ('valor_lancamento', models.DecimalField(decimal_places=2, default=0, max_digits=16, validators=[django.core.validators.MinLengthValidator(0.01)])),
                ('debito_credito', models.CharField(choices=[('D', 'Débito'), ('C', 'Crédito')], max_length=1)),
                ('historico_lancamento', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='PlanoDeConta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_conta', models.BigIntegerField(unique=True)),
                ('descricao', models.CharField(max_length=80)),
                ('tipo_conta', models.CharField(choices=[('A', 'Analítica'), ('S', 'Sintética')], max_length=1)),
                ('conta_ativa', models.BooleanField(default=True)),
                ('grau_conta', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(9)])),
                ('conta_saldo_balanco', models.BigIntegerField()),
                ('origem', models.CharField(choices=[('D', 'Débito'), ('C', 'Crédito')], max_length=1)),
                ('natureza', models.CharField(choices=[('D', 'Débito'), ('C', 'Crédito')], max_length=1)),
                ('data_inclusao', models.DateField()),
                ('conta_referencial_sped', models.CharField(max_length=20)),
                ('conta_superior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidade.PlanoDeConta')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globais.GlobEmpresas')),
            ],
        ),
        migrations.CreateModel(
            name='SaldosContabeis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_competencia', models.DateField()),
                ('origem', models.CharField(choices=[('D', 'Débito'), ('C', 'Crédito')], max_length=1)),
                ('saldo_anterior', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('total_debitos', models.DecimalField(decimal_places=2, default=0, max_digits=16, validators=[django.core.validators.MinLengthValidator(0.01)])),
                ('total_creditos', models.DecimalField(decimal_places=2, default=0, max_digits=16, validators=[django.core.validators.MinLengthValidator(0.01)])),
                ('codigo_conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidade.PlanoDeConta')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globais.GlobEmpresas')),
            ],
        ),
        migrations.AddField(
            model_name='lancamentoscontabil',
            name='codigo_conta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidade.PlanoDeConta'),
        ),
        migrations.AddField(
            model_name='lancamentoscontabil',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globais.GlobEmpresas'),
        ),
        migrations.AlterUniqueTogether(
            name='saldoscontabeis',
            unique_together=set([('empresa', 'data_competencia', 'codigo_conta')]),
        ),
        migrations.AlterUniqueTogether(
            name='planodeconta',
            unique_together=set([('empresa', 'codigo_conta')]),
        ),
        migrations.AlterIndexTogether(
            name='lancamentoscontabil',
            index_together=set([('empresa', 'codigo_conta', 'data_lancamento'), ('empresa', 'data_lancamento', 'codigo_conta')]),
        ),
    ]