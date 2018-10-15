from django.contrib import admin
from .models import Tenant, Bot, BotResponse

# Register your models here.

admin.site.register(Bot)
admin.site.register(BotResponse)
admin.site.register(Tenant)
