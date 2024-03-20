from django.contrib import admin

# Register your models here.

from .models import Produtos, Carrinhos
admin.site.register(Produtos)
admin.site.register(Carrinhos)
#


