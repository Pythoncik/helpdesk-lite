from django.urls import path
from . import views
urlpatterns=[path("",views.ticket_list,name="ticket_list"),path("register/",views.register,name="register"),path("tickets/new/",views.ticket_create,name="ticket_create"),path("tickets/<int:pk>/",views.ticket_detail,name="ticket_detail"),path("tickets/<int:pk>/edit/",views.ticket_update,name="ticket_update"),path("tickets/<int:pk>/delete/",views.ticket_delete,name="ticket_delete"),path("api/tickets/",views.ticket_api,name="ticket_api")]
