# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Member, Role, Roster, RosterAssignment
from .serializers import MemberSerializer, RoleSerializer, RosterSerializer, RosterAssignmentSerializer
from django.db.models import Count
from datetime import datetime, timedelta

# Viewset for Role
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# Viewset for Member
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# Custom Viewset for generating and displaying roster
class RosterViewSet(viewsets.ModelViewSet):
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer

    def create(self, request):
        """
        Expected input:
        {
            "sunday_date": "2025-05-04",
            "include_member_ids": [1, 2, 3],
            "exclude_member_ids": [4, 5]  # optional
        }
        """
        sunday_date = request.data.get("sunday_date")
        include_ids = request.data.get("include_member_ids", [])
        exclude_ids = request.data.get("exclude_member_ids", [])

        if not sunday_date or not include_ids:
            return Response({"error": "sunday_date and include_member_ids are required."}, status=400)

        # Remove excluded members from the pool
        available_members = Member.objects.filter(id__in=include_ids).exclude(id__in=exclude_ids)

        if not available_members.exists():
            return Response({"error": "No available members to assign."}, status=400)

        # Build a role-to-member map (ensuring one role per person)
        all_roles = Role.objects.all()
        used_members = set()
        assignments = []

        for role in all_roles:
            eligible_members = available_members.filter(roles=role).exclude(id__in=used_members)
            if eligible_members.exists():
                chosen_member = eligible_members.first()
                used_members.add(chosen_member.id)
                assignments.append((role, chosen_member))

        with transaction.atomic():
            roster = Roster.objects.create(sunday_date=sunday_date)
            for role, member in assignments:
                RosterAssignment.objects.create(roster=roster, role=role, member=member)

        return Response(RosterSerializer(roster).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        roster = self.get_object()
        serializer = RosterSerializer(roster)
        return Response(serializer.data)

    def update(self, request, pk=None):
        return Response({"error": "Roster updates are not supported. Delete and recreate instead."}, status=405)

    def destroy(self, request, pk=None):
        roster = self.get_object()
        roster.delete()
        return Response({"message": "Roster deleted successfully."}, status=204)