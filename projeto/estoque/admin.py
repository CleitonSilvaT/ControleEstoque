from django.contrib import admin
from .models import Estoque
from .models import EstoqueItens

# Register your models here.

# admin.site.register(Estoque)
# admin.site.register(EstoqueItens)

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'nf')
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'