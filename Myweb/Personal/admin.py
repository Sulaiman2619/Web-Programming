from django.contrib import admin
from .models import MemberImages
# Register your models here.

class  MemberAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(MemberImages, MemberAdmin)