from django.shortcuts import render
from django.utils import timezone
from .models import HistImage
from .forms import ContactForm
import random

from django.shortcuts import redirect

import sendgrid
import os
from sendgrid.helpers.mail import *

# Create your views here.

def homepage(request):
    HistImageDatabase = HistImage.objects.all()
    x = len(HistImageDatabase)
    RandomDailyImages = [HistImageDatabase[random.randint(0, x-1)],HistImageDatabase[random.randint(0, x-1)],HistImageDatabase[random.randint(0, x-1)],HistImageDatabase[random.randint(0, x-1)]]

    return render(request, 'history/index.html', {'RandomDailyImages' : RandomDailyImages})

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            content_subject = request.POST.get('content_subject', '')
            form_content = request.POST.get('content', '')

            sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
            from_email = Email(contact_email)
            to_email = Email("newbrunswickps@gmail.com")
            subject = str(content_subject)
            content = Content("text/plain", form_content)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)

            return redirect('contact')

    return render(request, 'history/contact.html', {'form': form_class})


