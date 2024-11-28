from rest_framework import serializers
from .models import Member, Role, Roster

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True)

    class Meta:
        model = Member
        fields = ['id', 'name', 'roles']

class RosterSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True)
    roles = RoleSerializer(many=True)

    class Meta:
        model = Roster
        fields = '__all__'
