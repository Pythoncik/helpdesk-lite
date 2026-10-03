from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404,redirect,render
from .forms import RegisterForm,TicketForm
from .models import Ticket
def register(request):
    if request.user.is_authenticated: return redirect("ticket_list")
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(); login(request,user); messages.success(request,"Konto erfolgreich erstellt."); return redirect("ticket_list")
    else: form=RegisterForm()
    return render(request,"registration/register.html",{"form":form})
@login_required
def ticket_list(request):
    tickets=Ticket.objects.filter(owner=request.user)
    query=request.GET.get("q","").strip(); status=request.GET.get("status",""); priority=request.GET.get("priority","")
    if query: tickets=tickets.filter(title__icontains=query)
    if status in {x[0] for x in Ticket.Status.choices}: tickets=tickets.filter(status=status)
    if priority in {x[0] for x in Ticket.Priority.choices}: tickets=tickets.filter(priority=priority)
    return render(request,"tickets/ticket_list.html",{"tickets":tickets,"query":query,"status":status,"priority":priority})
@login_required
def ticket_detail(request,pk):
    ticket=get_object_or_404(Ticket,pk=pk,owner=request.user)
    return render(request,"tickets/ticket_detail.html",{"ticket":ticket})
@login_required
def ticket_create(request):
    form=TicketForm(request.POST or None)
    if form.is_valid():
        ticket=form.save(commit=False); ticket.owner=request.user; ticket.save(); messages.success(request,"Ticket erstellt."); return redirect("ticket_list")
    return render(request,"tickets/ticket_form.html",{"form":form,"page_title":"Neues Ticket"})
@login_required
def ticket_update(request,pk):
    ticket=get_object_or_404(Ticket,pk=pk,owner=request.user)
    form=TicketForm(request.POST or None,instance=ticket)
    if form.is_valid(): form.save(); messages.success(request,"Ticket aktualisiert."); return redirect("ticket_detail",pk=ticket.pk)
    return render(request,"tickets/ticket_form.html",{"form":form,"page_title":"Ticket bearbeiten"})
@login_required
def ticket_delete(request,pk):
    ticket=get_object_or_404(Ticket,pk=pk,owner=request.user)
    if request.method=="POST": ticket.delete(); messages.success(request,"Ticket gelöscht."); return redirect("ticket_list")
    return render(request,"tickets/ticket_confirm_delete.html",{"ticket":ticket})
@login_required
def ticket_api(request):
    data=[{"id":t.id,"title":t.title,"category":t.category,"priority":t.priority,"status":t.status} for t in Ticket.objects.filter(owner=request.user)]
    return JsonResponse({"tickets":data})
