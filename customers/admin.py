from django.contrib import admin
from django.utils.html import format_html
from .models import Customer, LeadSource
# Register your models here.


class LeadSourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'action']
    list_filter = ['created_by', 'created_on']
    list_per_page = 10
    search_fields = ['name']

    actions = ["active_selected_record", 'inactive_selected_record']

    def action(self, obj):
        rst = 'NA'
        css = ""
        active = False

        if(obj.is_active):
            rst = 'Inactive'
            active = False
            css = 'btn-danger'
        else:
            active = True
            rst = 'Active'
            css = 'btn-success'
        return format_html(f'<button class="{css}" type="button" onclick="fn_ChangeStatus({obj.id},\'{active}\')">{rst}</button>')

    action.empty_value_display = 'NA'

    def active_selected_record(self, request, queryset):
        queryset.update(is_active=True)

    def inactive_selected_record(self, request, queryset):
        queryset.update(is_active=False)

    class Media:
        css = {
            'all': ('css/admin_helper.css',)
        }
        js = ("js/jquery.js", "js/admin_helper.js",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'designation', 'email',
                    'mobile', 'organization', 'lead_source', 'action']
    list_filter = ['created_by', 'created_on']
    list_per_page = 10
    search_fields = ['name', 'code', 'designation', 'email', 'mobile', ]

    actions = ["active_selected_record", 'inactive_selected_record']

    def action(self, obj):
        rst = 'NA'
        css = ""
        active = False

        if(obj.is_active):
            rst = 'Inactive'
            active = False
            css = 'btn-danger'
        else:
            active = True
            rst = 'Active'
            css = 'btn-success'
        return format_html(f'<button class="{css}" type="button" onclick="fn_ChangeStatus({obj.id},\'{active}\')">{rst}</button>')

    action.empty_value_display = 'NA'

    def active_selected_record(self, request, queryset):
        queryset.update(is_active=True)

    def inactive_selected_record(self, request, queryset):
        queryset.update(is_active=False)

    class Media:
        css = {
            'all': ('css/admin_helper.css',)
        }
        js = ("js/jquery.js", "js/admin_helper.js",)

    def save_model(self, request, obj, form, change):
        from customers.models import Customer
        # from django.db.models import Count
        obj.code = maxCode(Customer.objects.all().count(),6,'PRANSON')
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(LeadSource, LeadSourceAdmin)


def maxCode(total, digit, prefix):
    total = str(total)
    add = digit-len(total)
    return prefix+("0"*add)+total
