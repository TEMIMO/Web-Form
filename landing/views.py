from django.shortcuts import render
from .forms import SubscriberForm
import os
import threading
from django.core.mail import EmailMessage

def printit():
    threading.Timer(100.0, printit).start()
    if not os.listdir('Pr2/files/media/csv'):
        print('COOL!')
    else:
        print('FUCK!')
printit()
em = EmailMessage(subject='Test', body='Test', to=['artemymif@gmail.com'])
#em.send()

def landing(request, Id = None ):
    form = SubscriberForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form = form.save()
    return render(request, 'landing/landing.html', locals())


