from django.contrib import admin
from .models import Asset, AssetCategory, AssetType, AssetTransfer, AssetInspection, AssetDepreciation


@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    search_fields = ['name', 'category']


@admin.register(AssetType)
class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name']


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['asset_tag_number', 'asset_id', 'description', 'status', 'condition', 'custodian']
    list_filter = ['category', 'status', 'condition', 'created_at']
    search_fields = ['asset_id', 'asset_tag_number', 'description', 'serial_number']
    readonly_fields = ['asset_id', 'created_at', 'updated_at']
    fieldsets = (
        ('Identification', {'fields': ('asset_id', 'asset_tag_number', 'barcode', 'qr_code')}),
        ('Classification', {'fields': ('category', 'asset_type', 'description', 'serial_number', 'make_model')}),
        ('Financial', {'fields': ('purchase_date', 'purchase_cost', 'supplier', 'funding_source', 'current_book_value', 'depreciation_method', 'useful_life_years', 'residual_value')}),
        ('Location & Responsibility', {'fields': ('facility', 'venue', 'building', 'room_area', 'custodian', 'department', 'responsible_officer')}),
        ('Condition & Maintenance', {'fields': ('condition', 'status', 'maintenance_schedule', 'warranty_end_date', 'next_service_date')}),
        ('Disposal', {'fields': ('disposal_date', 'disposal_method', 'tender_reference', 'disposal_value')}),
        ('Audit', {'fields': ('created_by', 'created_at', 'updated_at')}),
    )


@admin.register(AssetTransfer)
class AssetTransferAdmin(admin.ModelAdmin):
    list_display = ['asset', 'from_custodian', 'to_custodian', 'transfer_date']
    list_filter = ['transfer_date']
    search_fields = ['asset__asset_tag_number', 'from_custodian__username', 'to_custodian__username']
    readonly_fields = ['transfer_date', 'created_by']


@admin.register(AssetInspection)
class AssetInspectionAdmin(admin.ModelAdmin):
    list_display = ['asset', 'inspection_date', 'status', 'condition_after', 'inspector']
    list_filter = ['status', 'inspection_date', 'condition_after']
    search_fields = ['asset__asset_tag_number', 'observations']


@admin.register(AssetDepreciation)
class AssetDepreciationAdmin(admin.ModelAdmin):
    list_display = ['asset', 'year', 'depreciation_amount', 'book_value_end']
    list_filter = ['year']
    search_fields = ['asset__asset_tag_number']
    readonly_fields = ['calculated_at']
