from django.db import models
from globais.models import GlobEmpresas

from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator

DEBITO_CREDITO_CHOICES = (('D', 'Débito'), ('C', 'Crédito'))
TIPO_CONTA_CHOICES = (('A', 'Analítica'), ('S', 'Sintética'))


# **********************************************************************************************
# ARQUIVO DE CONTAS CONTABEIS
# (usesoft=KCGI03)
# **********************************************************************************************
class PlanoDeConta(models.Model):
    empresa = models.ForeignKey(GlobEmpresas)
    codigo_conta = models.BigIntegerField(unique=True, null=False)
    descricao = models.CharField(max_length=80, null=False)
    # [A] Analítica [S] Sintética [G] Grupo
    tipo_conta = models.CharField(max_length=1, choices=TIPO_CONTA_CHOICES)
    # True = ativa False = inativa
    conta_ativa = models.BooleanField(default=True)
    grau_conta = models.PositiveSmallIntegerField(null=False, validators=[MaxValueValidator(9)])
    # codigo da conta de grau imediatamente superior ao grau desta conta
    # tem como objetivo acumular valores no plano de contas automaticamente a cada lançamento
    conta_superior = models.ForeignKey('self')
    # codigo da conta do passivo para onde irão automaticamente os saldos de receita e despesa
    # quando for feita a apuração do resultado periódica
    # apuração zera receita e despesa e transfere resultado para conta de balanço
    conta_saldo_balanco = models.BigIntegerField(null=False)
    # "M" = RAZAO E DIÁRIO SÃO CONCENTRADOS EM 1 LANÇAMENTO POR MÊS
    # "D" = RAZAO E DIÁRIO SERÃO CONCENTRADOS EM LANÇAMENTO POR DIA
    # ****************************************************************
    # diario_razao = models.CharField(max_length=1, null=False)
    # "D" = PARA CONTA PREDOMINANTEMENTE DEVEDORA
    # "C" = PREDOMINAÂNCIA CREDORA
    # ****************************************************************
    origem = models.CharField(max_length=1, choices=DEBITO_CREDITO_CHOICES)
    natureza = models.CharField(max_length=1, choices=DEBITO_CREDITO_CHOICES)

    data_inclusao = models.DateField(null=False)
    conta_referencial_sped = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.codigo_conta

    class Meta:
        unique_together = (('empresa', 'codigo_conta'),)


# **********************************************************************************************
# ARQUIVO DE LANÇAMENTOS CONTABEIS DO SISTEMA
# (usesoft=KCGI03)
# **********************************************************************************************
class LancamentoContabil(models.Model):
    empresa = models.ForeignKey(GlobEmpresas)
    codigo_conta = models.ForeignKey(PlanoDeConta)

    data_competencia = models.DateField(null=False)
    data_lancamento = models.DateField(auto_now=True)
    numero_documento = models.CharField(max_length=12, null=False)
    # saldo anterior deverá estar replicado na tabela de saldos mensais das contas contabeis
    valor_lancamento = models.DecimalField(max_digits=16, decimal_places=2, default=0,
                                           validators=[MinLengthValidator(0.01)])

    #  "D" = Debito contábil  (+) "C" = Credito contábil (-)
    debito_credito = models.CharField(max_length=1, choices=DEBITO_CREDITO_CHOICES)
    # no lancamento do histórico permitir ao usuario selecionar um codigo de históricos de tabela de históricos
    # permitir usar codigos da tabela Materiais/MensagensPadroes
    historico_lancamento = models.TextField(max_length=400, null=False)

    def __str__(self):
        return self.codigo_conta

    class Meta:
        # emissao do razao & emissao do diario
        index_together = (("empresa", 'codigo_conta', 'data_lancamento'),
                          ("empresa", 'data_lancamento', 'codigo_conta'))


# **********************************************************************************************
# SALDOS MENSAIS DAS CONTAS CONTABEIS
# (usesoft=KCGI03S)
# **********************************************************************************************
class SaldoContabil(models.Model):
    empresa = models.ForeignKey(GlobEmpresas)
    # neste campo data o dia será sempre o último dia do mes
    data_competencia = models.DateField(null=False)
    codigo_conta = models.ForeignKey(PlanoDeConta)
    origem = models.CharField(max_length=1, choices=DEBITO_CREDITO_CHOICES)

    saldo_anterior = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    total_debitos = models.DecimalField(max_digits=16, decimal_places=2, default=0,
                                        validators=[MinLengthValidator(0.01)])
    total_creditos = models.DecimalField(max_digits=16, decimal_places=2, default=0,
                                         validators=[MinLengthValidator(0.01)])

    def __str__(self):
        return self.codigo_conta

    def saldo_atual(self):
        if self.origem == 'D':
            return self.saldo_anterior + self.total_debitos - self.total_creditos
        else:
            return self.saldo_anterior + self.total_creditos - self.total_debitos

    class Meta:
        # emissao do balanco e balancete
        unique_together = ("empresa", 'data_competencia', 'codigo_conta',)
