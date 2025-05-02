# serializers.py
from rest_framework import serializers
from .models import Member, Role, Roster, RosterAssignment

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True)

    class Meta:
        model = Member
        fields = ['id', 'name', 'roles']

class RosterAssignmentSerializer(serializers.ModelSerializer):
    member = serializers.StringRelatedField()
    role = serializers.StringRelatedField()

    class Meta:
        model = RosterAssignment
        fields = ['member', 'role']

class RosterSerializer(serializers.ModelSerializer):
    assignments = RosterAssignmentSerializer(many=True, read_only=True)

    class Meta:
        model = Roster
        fields = ['id', 'sunday_date', 'assignments']
