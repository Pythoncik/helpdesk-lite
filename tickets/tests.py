from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Ticket
class TicketFlowTests(TestCase):
    def setUp(self): self.user=User.objects.create_user(username="maxim",password="StrongTestPassword123!")
    def test_registration_page_exists(self): self.assertEqual(self.client.get(reverse("register")).status_code,200)
    def test_user_can_create_ticket(self):
        self.client.login(username="maxim",password="StrongTestPassword123!")
        r=self.client.post(reverse("ticket_create"),{"title":"Computer does not start","description":"The PC shows no image.","category":"hardware","priority":"high","status":"open"})
        self.assertRedirects(r,reverse("ticket_list")); self.assertEqual(Ticket.objects.count(),1); self.assertEqual(Ticket.objects.first().owner,self.user)
    def test_user_only_sees_own_tickets(self):
        other=User.objects.create_user(username="other",password="StrongTestPassword123!"); Ticket.objects.create(owner=other,title="Private ticket",description="Not visible")
        self.client.login(username="maxim",password="StrongTestPassword123!"); r=self.client.get(reverse("ticket_list")); self.assertNotContains(r,"Private ticket")
    def test_json_endpoint_returns_user_tickets(self):
        self.client.login(username="maxim",password="StrongTestPassword123!"); Ticket.objects.create(owner=self.user,title="Wi-Fi issue",description="Connection is unstable."); r=self.client.get(reverse("ticket_api")); self.assertEqual(r.status_code,200); self.assertEqual(len(r.json()["tickets"]),1)
