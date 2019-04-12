from django.shortcuts import render
from .forms import SubscriberForm
def landing(request, Id = None ):
    form = SubscriberForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form = form.save()
    return render(request, 'landing/landing.html', locals())


