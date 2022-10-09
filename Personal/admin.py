from django.contrib import admin
from .models import *
# Register your models here.
class  MemberImagesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(MemberImages, MemberImagesAdmin)


class  ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Project1, ProjectAdmin)

admin.site.register(Student)

admin.site.register(IndexImage)

