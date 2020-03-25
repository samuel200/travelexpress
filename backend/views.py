from django.shortcuts import render, redirect
from mailjet_rest import Client
import os

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


def contact_view(request):
    if request.method == 'POST':
        api_key = 'b19c65277284563a4f0aa934cc7d7814'
        api_secret = '4974dd6642ad5fbddd4073325ede6621'
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "travelexpress@support.com",
                        "Name": "harrison"
                    },
                    "To": [
                        {
                            "Email": "frankharrisonmd250@gmail.com",
                            "Name": "harrison"
                        }
                    ],
                    "Subject": "Greetings from Mailjet.",
                    "TextPart": "My first Mailjet email",
                    "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
                    "CustomID": "AppGettingStartedTest"
                }
            ]
        }
        result = mailjet.send.create(data=data)
        print (result.status_code)
        print (result.json())

    return render(request, 'contact.html')


def destination_view(request):
    return render(request, 'travel_destination.html')
