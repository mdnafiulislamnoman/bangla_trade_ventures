from django.contrib import admin
from .models import User, SupplierProfile

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'is_staff']
    list_filter = ['role']

@admin.register(SupplierProfile)
class SupplierProfileAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'user', 'is_verified', 'created_at']
    list_filter = ['is_verified']
    actions = ['verify_suppliers']

    def verify_suppliers(self, request, queryset):
        queryset.update(is_verified=True)
    verify_suppliers.short_description = "Verify selected suppliers"