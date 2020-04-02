from django.shortcuts import render, redirect
# from mailjet_rest import Client
import os
import requests

from .models import Flight


def index_view(request):
    return render(request, 'index.html')


def booking_view(request):
    if request.method == "POST":
        return redirect('destination')
    return render(request, 'web/index.html')


def tracking_view(request):
    if request.method == "POST":
        try:
            flight = Flight.objects.get(number=int(request.POST.get("tracking")))
            return render(request, 'tracking.html', {"flight": flight})

        except Flight.DoesNotExist:
            return render(request, 'tracking.html', {"error_message": "Flight does not exist."})

    return render(request, 'tracking.html')

def about_view(request):
    return render(request, 'about.html')

def send_simple_message(name, email, subject, message):
	return requests.post(
		"https://api.mailgun.net/v3/sandboxcc255dee358f491d9965eeeeff0d07b3.mailgun.org/messages",
		auth=("api", "8b3067f3767ffdb9c02afda45dc02b7d-ed4dc7c4-56618e3c"),
		data={"from": "support@sandboxcc255dee358f491d9965eeeeff0d07b3.mailgun.org",
			"to": [email],
			"subject": subject,
			"text": f"Name: { name }\nMessage: { message }"})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        req = send_simple_message(name, email, subject, message)
        return render(request, 'contact.html', {"req": req})
    return render(request, 'contact.html')


def destination_view(request):
    return render(request, 'travel_destination.html')
