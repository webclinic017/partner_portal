from django.contrib import admin
from .models import CustomerUser, Partner, PartnerUser, MonitorNetwork


admin.site.register(MonitorNetwork)
# admin.site.register(Partner)
# admin.site.register(PartnerUser)

@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'status','provided_by', 'is_excluded')
    list_filter = ('is_excluded', 'status')
    # search_fields = ('synsuite_contract_code',)
    # date_hierarchy = 'created_at'



@admin.register(PartnerUser)
class PartnerUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'partner')
    # list_filter = ('doc_type',)
    # date_hierarchy = 'created_at'

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('title', )