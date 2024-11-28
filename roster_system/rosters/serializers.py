from rest_framework import serializers
from .models import Member, Role, Roster

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class MemberSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)

    class Meta:
        model = Member
        fields = ['id', 'name', 'roles']

class RosterSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True)
    roles = RoleSerializer(many=True)

    class Meta:
        model = Roster
        fields = ['id', 'sunday_date', 'members', 'roles']
