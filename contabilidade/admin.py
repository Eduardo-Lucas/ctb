from django.contrib import admin
from contabilidade.models import PlanoDeConta, LancamentoContabil, SaldoContabil

# Register your models here.

admin.site.register(PlanoDeConta)
admin.site.register(LancamentoContabil)
admin.site.register(SaldoContabil)
