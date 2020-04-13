from django.contrib import admin
from .models import OrganizationIndustry, OrganizationOwnership, OrganizationStatus, OrganizationType, Organization
from django.utils.html import format_html
# Register your models here.


class OrganizationIndustryAdmin(admin.ModelAdmin):
    list_display = ['name', 'action']
    list_filter = ['created_by', 'created_on']
    list_per_page=10

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


class OrganizationOwnershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'action']
    list_filter = ['created_by', 'created_on']
    list_per_page=10
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


class OrganizationStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'action']
    list_filter = ['created_by', 'created_on']
    list_per_page=10
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


class OrganizationTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'action']
    list_filter = ['created_by', 'created_on']
    list_per_page=10
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


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile_no', 'organization_ownership', 'organization_type', 'organization_industry', 'organization_status', 'action']
    list_filter = ['created_by', 'created_on']
    list_per_page=10
    search_fields = ['name', 'mobile_no','organization_ownership_name', 'organization_type_name', 'organization_industry_name', 'organization_status_name']

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

admin.site.register(OrganizationIndustry, OrganizationIndustryAdmin)
admin.site.register(OrganizationOwnership, OrganizationOwnershipAdmin)
admin.site.register(OrganizationStatus, OrganizationStatusAdmin)
admin.site.register(OrganizationType, OrganizationTypeAdmin)
admin.site.register(Organization, OrganizationAdmin)
