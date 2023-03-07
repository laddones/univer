from django.contrib import admin
from admin_panel.models.client import Client, Links, LinkClientStatus


# Register your models here.


class ClientTelegramAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'status', 'time_create']
    list_filter = ('time_create', 'status')
    search_fields = ('user_id', 'username')
    # readonly_fields = ('user_id',)
    ordering = ['-status']


class LinksAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'link_type', 'link_status', 'time_create']
    list_filter = ('link_type', 'link_status', 'time_create')
    ordering = ['-time_create']
    exclude = ('admin',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        if formset.model == Links:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                print(instance.first_name)
                instance.save()
        else:
            formset.save()


class ClientLink(admin.ModelAdmin):
    list_display = ['link_status', 'client', 'link']


admin.site.register(LinkClientStatus, ClientLink)
admin.site.register(Client, ClientTelegramAdmin)
admin.site.register(Links, LinksAdmin)