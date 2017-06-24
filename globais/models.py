from django.db import models

TIPO_EMPRESA_CHOICES = (("SN", 'Simples Nacional'), ("LP", 'Lucro presumido'), ("LR", 'Lucro REAL'))
SIM_NAO_CHOICES = (('S', 'Sim'), ('N', 'Não'))

# **********************************************************************************************
# ARQUIVO DE EMPRESAS USUARIAS DO SISTEMA - TABELAS GENERICAS DO SISTEMA USESOFT-R3
# (usesoft=KSBIUS)
# Tabela base default = usesoft-R3\TabelasGlobais\glob_naturezas_de_custos.txt
# **********************************************************************************************
class GlobEmpresas(models.Model):
    codigo = models.CharField(max_length=15, null=False, default="MATRIZ")
    razao_social = models.CharField(max_length=60, null=False)
    nome_fantasia = models.CharField(max_length=60, null=False)
    endereco = models.CharField(max_length=60, null=False)
    complemento = models.CharField(max_length=60)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30, null=False)
    # cep = models.PositiveIntegerField(null=False, validators=[MaxValueValidator(99999999)])
    # municipio = models.ForeignKey(GlobMunicipios)
    # estado = models.ForeignKey(GlobCodEstados)
    telefone1 = models.CharField(max_length=15)
    telefone2 = models.CharField(max_length=15)

    data_processamento = models.DateField(max_length=8)
    data_competencia = models.DateField(max_length=8)

    # natureza_juridica = models.ForeignKey(GlobNaturezasJuridicas)

    site_empresa = models.CharField(max_length=100)
    email_empresa = models.CharField(max_length=100)
    cnpj = models.BigIntegerField(unique=True, null=False)
    inscricao_estadual = models.CharField(max_length=15)
    inscricao_municipal = models.CharField(max_length=15)
    # codigo_cnae = models.ForeignKey(GlobCodigosCnaes)
    # "SN" - simples nacional
    # "LP" - Lucro presumido
    # "LR" - Lucro REAL
    tipo_empresa = models.CharField(max_length=2, choices=TIPO_EMPRESA_CHOICES, default="LR")
    # gerente_empresa = models.ForeignKey(Usuario)
    # diretor_empresa = models.ForeignKey(Usuario)
    # contador_empresa = models.ForeignKey(Usuario)

    # configuracoes customizaveis por empresa
    # "S" neste campo para que sistema agrupe numero de itens na venda balcao por codigo se houver codigos repetidos
    agrupa_itens_pedido = models.CharField(max_length=1, choices=SIM_NAO_CHOICES, default="N")

    # "S" neste campo para que o cliente seja automaticamente bloqueado durante"
    # o fechamento de uma venda no balcao ou no caixa
    bloqueia_clientes_em_atraso = models.CharField(max_length=1, choices=SIM_NAO_CHOICES, default="N")

    def __str__(self):
        return self.codigo

    class Meta:
        ordering = ('codigo',)
