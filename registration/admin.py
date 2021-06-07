from django.contrib import admin
from . import models

class Student(admin.ModelAdmin):
    list_display = [field.name for field in models.Student._meta.get_fields() if field.name != 'id']

    def has_view_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request, obj=None):
        return True

    def get_queryset(self, request):
        queryset = super(Student, self).get_queryset(request)
        return queryset.exclude(id__lt=46)

admin.register(models.Student)(Student)
