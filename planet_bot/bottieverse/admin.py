from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as TenantUserAdmin

# from .forms import TenantChangeForm, TenantCreationForm
from django.contrib.auth.models import User

from .models import *


# Register your models here.

class TenantInline(admin.StackedInline):
    model = Tenant
    can_delete = False
    verbose_name = 'tenant'
    verbose_name_plural = 'tenants'


class UserAdmin(TenantUserAdmin):
    inlines = (TenantInline,)


# admin.site.register(Tenant)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Bot)
admin.site.register(Response)
admin.site.register(Intent)
admin.site.register(TrainingPhrase)
admin.site.register(Action)
admin.site.register(Parameter)