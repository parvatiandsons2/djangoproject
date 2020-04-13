from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import Slider, Testimonial, Alert, ContactUs, TrustedBy, CompanyStats
import datetime
# Register your models here.


class SliderAdmin(admin.ModelAdmin):
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


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'company', 'action']
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


class AlertAdmin(admin.ModelAdmin):
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


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'action']
    list_filter = ['created_on']
    list_per_page = 10
    search_fields = ['name', 'mobile', 'email']

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
        obj.is_active = True
        obj.created_on = datetime.datetime.now()
        super().save_model(request, obj, form, change)


class TrustedByAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'action']
    list_filter = ['created_on']
    list_per_page = 10
    search_fields = ['name', 'link']

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


class CompanyStatsAdmin(admin.ModelAdmin):
    list_display = ['name', 'customers', 'happy_clients', 'projects', 'enquiry', 'action']
    list_filter = ['created_on']
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


admin.site.register(Slider, SliderAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(TrustedBy, TrustedByAdmin)
admin.site.register(CompanyStats, CompanyStatsAdmin)
