from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Deal
from datetime import datetime
import pytz
from django.utils import timezone
from .forms import DealForm
utc=pytz.UTC
# Create your views here.

def home(request):
    today_date_time = timezone.make_aware(datetime.now(), timezone.get_default_timezone())
    deals = Deal.objects.all()
    qualified_deals = []
    for deal in deals:
        if today_date_time>deal.start_date_time and today_date_time<deal.end_date_time:
            qualified_deals.append(deal)

    print("Today date and time:", today_date_time, deal.start_date_time)
    return  render(request,'app/home.html',{"deals":qualified_deals})

def create(request):
    if request.method == "POST":
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"deal saved successfully..")
            return redirect(reverse('home'))
        else:
            messages.error("check data carefully..")
            return redirect(reverse('create'))
    else:
        form = DealForm()
        return render(request,'app/dealcreate.html',{'form':form})