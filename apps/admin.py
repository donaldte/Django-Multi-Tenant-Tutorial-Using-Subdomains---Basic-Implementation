from django.contrib import admin
from .models import Tenant, TenantAwareMode, Member
# Register your models here.

admin.site.register(Tenant)
admin.site.register(Member)

