from django.contrib import admin
from . models import Transcation
# Register your models here.
from import_export import resources
from import_export.admin import ExportMixin
class TranscationResource(resources.ModelResource):
    class Meta:
        model = Transcation
        fields = ('id', 'user', 'title', 'amount', 'date', 'transcation_type', 'category')
class TranscationAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TranscationResource
    list_display = ('id', 'user', 'title', 'amount', 'date', 'transcation_type', 'category')
    search_fields = ('title', 'user__username', 'category')

admin.site.register(Transcation, TranscationAdmin)
