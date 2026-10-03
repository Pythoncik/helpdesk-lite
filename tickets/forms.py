from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket
class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True,label="E-Mail")
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        labels={"username":"Benutzername"}
class TicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=["title","description","category","priority","status"]
        labels={"title":"Titel","description":"Beschreibung","category":"Kategorie","priority":"Priorität","status":"Status"}
        widgets={"description":forms.Textarea(attrs={"rows":6})}
