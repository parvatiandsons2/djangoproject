from django.contrib import admin
from .models import Vendor
from django.utils.html import format_html
# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile_no', 'email', 'action']
    list_filter=['created_by', 'created_on']
    list_per_page=10
    search_fields = ['name','mobile_no', 'email']

    actions = ["active_selected_record", 'inactive_selected_record']

    def action(self, obj):
        rst='NA'
        css=""
        active=False

        if(obj.is_active):
            rst='Inactive'
            active=False
            css='btn-danger'
        else:
            active=True
            rst='Active'
            css='btn-success'
        return format_html(f'<button class="{css}" type="button" onclick="fn_ChangeStatus({obj.id},\'{active}\')">{rst}</button>')

    action.empty_value_display = 'NA'


    def active_selected_record(self, request, queryset):
        queryset.update(is_active=True)
    
    def inactive_selected_record(self, request, queryset):
        queryset.update(is_active=False)

    class Media:
        css={
            'all':('css/admin_helper.css',)
        }
        js = ("js/jquery.js","js/admin_helper.js",)


    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Vendor,VendorAdmin)