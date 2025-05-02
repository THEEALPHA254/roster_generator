# models.py
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    roles = models.ManyToManyField('Role')

    def __str__(self):
        return self.name

class Roster(models.Model):
    sunday_date = models.DateField()

    def __str__(self):
        return f"Roster for {self.sunday_date}"

    def member_roles(self):
        # Safely list assigned roles per member in this roster
        assignments = self.assignments.select_related('member', 'role')
        return "; ".join(f"{a.member.name}: {a.role.name}" for a in assignments)

    member_roles.short_description = "Assignments"

class RosterAssignment(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE, related_name='assignments')
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('roster', 'role')  # Ensure each role is assigned once per roster

    def __str__(self):
        return f"{self.member.name} - {self.role.name} ({self.roster.sunday_date})"
