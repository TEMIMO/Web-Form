from django.shortcuts import render
from .forms import SubscriberForm
import os
import threading
from django.core.mail import EmailMessage
from. import validation



# def printit():
#     threading.Timer(10.0, printit).start()
#     if not os.listdir('landing/input_user'):
#         print('COOL!')
#     else:
#         print('FUCK!')
#         validation.valid('landing/input_user')
#         em = EmailMessage(subject='Test', body='Test', to=['artemymif@gmail.com'])
#         em.attach_file(r'C:\Users\Артемий\PycharmProjects\Pr2\landing\input_user\result.txt')
#         em.send()
#
# printit()
def landing(request, Id = None ):
    form = SubscriberForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form = form.save()
    return render(request, 'landing/landing.html', locals())


