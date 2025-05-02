# admin.py
from django.contrib import admin
from .models import Roster, Member, Role

@admin.register(Roster)
class RosterAdmin(admin.ModelAdmin):
    list_display = ('sunday_date', 'member_roles')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)