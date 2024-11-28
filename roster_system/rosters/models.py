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
    members = models.ManyToManyField(Member, related_name='rosters')
    roles = models.ManyToManyField(Role, related_name='rosters')

    def __str__(self):
        return f"Roster for {self.sunday_date}"
