from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user has already made inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(
                listing_id=listing_id, user_id=user_id).exists()
            if has_contacted:
                messages.error(
                    request, "An inquiry for this listing has already been made!")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, phone=phone, message=message,
                          user_id=user_id, realtor_email=realtor_email, name=name, email=email)
        contact.save()

        # send email
        send_mail(
            'BTRE - Property Listing Inquiry',
            'A new inquiry is received on BTRE for listing ' + listing,
            'doe817615@gmail.com',
            [realtor_email, 'abbas.devcode@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted')
        return redirect('/listings/'+listing_id)
