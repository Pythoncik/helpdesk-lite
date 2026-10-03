from django.conf import settings
from django.db import migrations,models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial=True
    dependencies=[migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations=[migrations.CreateModel(name="Ticket",fields=[("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),("title",models.CharField(max_length=120)),("description",models.TextField()),("category",models.CharField(choices=[("hardware","Hardware"),("software","Software"),("network","Netzwerk"),("account","Benutzerkonto"),("other","Sonstiges")],default="other",max_length=20)),("priority",models.CharField(choices=[("low","Niedrig"),("medium","Mittel"),("high","Hoch")],default="medium",max_length=10)),("status",models.CharField(choices=[("open","Offen"),("progress","In Bearbeitung"),("resolved","Gelöst")],default="open",max_length=10)),("created_at",models.DateTimeField(auto_now_add=True)),("updated_at",models.DateTimeField(auto_now=True)),("owner",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="tickets",to=settings.AUTH_USER_MODEL))],options={"ordering":["-created_at"]})]
