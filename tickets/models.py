from django.contrib.auth.models import User
from django.db import models
class Ticket(models.Model):
    class Status(models.TextChoices):
        OPEN="open","Offen"
        IN_PROGRESS="progress","In Bearbeitung"
        RESOLVED="resolved","Gelöst"
    class Priority(models.TextChoices):
        LOW="low","Niedrig"
        MEDIUM="medium","Mittel"
        HIGH="high","Hoch"
    class Category(models.TextChoices):
        HARDWARE="hardware","Hardware"
        SOFTWARE="software","Software"
        NETWORK="network","Netzwerk"
        ACCOUNT="account","Benutzerkonto"
        OTHER="other","Sonstiges"
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="tickets")
    title=models.CharField(max_length=120)
    description=models.TextField()
    category=models.CharField(max_length=20,choices=Category.choices,default=Category.OTHER)
    priority=models.CharField(max_length=10,choices=Priority.choices,default=Priority.MEDIUM)
    status=models.CharField(max_length=10,choices=Status.choices,default=Status.OPEN)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: ordering=["-created_at"]
    def __str__(self): return f"#{self.pk} {self.title}"
