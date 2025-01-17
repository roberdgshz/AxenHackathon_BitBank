from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from .models import Contact
from django.db.models import Q


# Create your views here.
Account = get_user_model()

@login_required
def contact_list(request):
    contacts = Contact.objects.filter(owner=request.user).select_related('contact_user')
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

@login_required
def add_contact(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')  # Puede ser email o username
        nickname = request.POST.get('nickname')

        try:
            # Buscar usuario por email o username
            contact_user = Account.objects.filter(
                Q(email=identifier) | 
                Q(accountusername=identifier)
            ).first()

            if contact_user:
                if contact_user == request.user:
                    messages.error(request, "You can't add yourself as a contact")
                    return redirect('contacts:contact_list')

                contact = Contact(
                    owner=request.user,
                    contact_user=contact_user,
                    nickname=nickname if nickname else None
                )
                contact.save()
            else:
                messages.error(request, "User not found.")
        except IntegrityError:
            messages.error(request, "The contact alredy exist.")
        
        return redirect('contacts:contact_list')
    
    return render(request, 'contacts/add_contact.html')

@login_required
def remove_contact(request, contact_id):
    contact = get_object_or_404(Contact, contactid=contact_id, owner=request.user)
    contact.delete()
    return redirect('contacts:contact_list')