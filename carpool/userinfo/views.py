from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def info(request):
    context = {'page':'info'}
    return render(request,"info.html",context)

def provider(request):
    context = {'page':'provider'}
    return render(request,"provider.html",context)

def receiver(request):
    context = {'page':'receiver'}
    return render(request,"receiver.html",context)

def allusers(request):
    if request.method == "POST":
        if 'p_name' in request.POST and 'p_email' in request.POST and 'car_name' in request.POST and 'seats_available' in request.POST:
            # Process provider data
            p_name = request.POST['p_name']
            p_email = request.POST['p_email']
            car_name = request.POST['car_name']
            seats_available = request.POST['seats_available']
            Provider.objects.create(p_name=p_name, p_email=p_email, car_name=car_name, seats_available=seats_available)
            return redirect('/provider/allusers/')
        elif 'r_name' in request.POST and 'r_email' in request.POST:
            # Process receiver data
            r_name = request.POST['r_name']
            r_email = request.POST['r_email']
            Receiver.objects.create(r_name=r_name, r_email=r_email)
            return redirect('/receiver/allusers/')

    # Fetch data from both models
    provider_data = Provider.objects.all()
    receiver_data = Receiver.objects.all()

    # Combine data into a single context dictionary
    context = {'provider_data': provider_data, 'receiver_data': receiver_data}

    # Render the template with the combined data
    return render(request, 'allusers.html', context)