import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HeaderVideo, HeaderImage
from django.contrib import messages
from .forms import QuoteMotorForm, QuoteCarForm, EnquiryForm, EnquiryRenewCarForm, EnquiryRenewMotorcycleForm, ApplyForm, ApplyCOEForm
from datetime import datetime


def home(request):
    apply_form = ApplyForm()
    context = {
        'apply_form': apply_form,
    }
    return render(request, 'apploan/home.html', context)

def financeUsed(request):
    header_image = HeaderImage.objects.filter(template_type='used_cm').first()
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'header_image': header_image,
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }
    return render(request, 'apploan/financing/used-cm-loan.html', context)


def financeDirect(request):
    header_image = HeaderImage.objects.filter(template_type='direct_bs').first()
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'header_image': header_image,
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }
    return render(request, 'apploan/financing/direct-bs-loan.html', context)

def financeNew(request):
    header_image = HeaderImage.objects.filter(template_type='new_cm').first()
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'header_image': header_image,
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }
    return render(request, 'apploan/financing/new-cm-loan.html', context)

def financeCOECar(request):
    header_image = HeaderImage.objects.filter(template_type='coe_car').first()
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'header_image': header_image,
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }
    return render(request, 'apploan/financing/coe-car-loan.html', context)

def financeRefinance(request):
    apply_form = ApplyForm()

    context = {
        'apply_form': apply_form,
    }
    
    return render(request, 'apploan/financing/car-refinancing.html', context)

def financeInHouse(request):
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }
    return render(request, 'apploan/financing/in-house.html', context)

def financePHVCar(request):
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }
    return render(request, 'apploan/financing/phv-car-loan.html', context)

# COE Renewal
def COERenewCar(request):
    if request.method == "POST":
        form = EnquiryRenewCarForm(request.POST, initial={'loan_type': 'car'})
        if form.is_valid():
            form.save()
            return redirect(f"{request.path}?submitted=true")
    else:
        form = EnquiryRenewCarForm(initial={'loan_type': 'car'})
    return render(request, "apploan/coe/coe-renew-car.html", {"form": form, "loan_type": "car"})


def COERenewMoto(request):
    if request.method == "POST":
        form = EnquiryRenewMotorcycleForm(request.POST, initial={'loan_type': 'motorcycle'})
        if form.is_valid():
            form.save()
            return redirect(f"{request.path}?submitted=true")
    else:
        form = EnquiryRenewMotorcycleForm(initial={'loan_type': 'motorcycle'})
    return render(request, "apploan/coe/coe-renew-motor.html", {"form": form, "loan_type": "motorcycle"})

# Insurance
def insCar(request):
    video = HeaderVideo.objects.filter(insurance_type='car').first()
    form = QuoteCarForm()
    return render(request, 'apploan/insurance/ins-car.html', {'video': video, 'form': form})

def insMotor(request):
    video = HeaderVideo.objects.filter(insurance_type='motorcycle').first()
    form = QuoteMotorForm()
    return render(request, 'apploan/insurance/ins-motor.html', {'video': video, 'form': form})

# Rates
def rates(request):
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }
    return render(request, 'apploan/rates.html', context)

# Guides
def guidesCalc(request):
    return render(request, 'apploan/guides/loan-calc.html')

def guidesFaq(request):
    return render(request, 'apploan/guides/loan-faq.html')

def guidesInstall(request):
    return render(request, 'apploan/guides/loan-installment.html')

def guidesPay(request):
    return render(request, 'apploan/guides/loan-pay.html')

def formCar(request):
    if request.method == 'POST':
        form = ApplyCOEForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.vehicle_type = 'car'
            instance.save()

            next_url = request.POST.get('next', '/')
            return redirect(f"{next_url}?submitted=true")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ApplyCOEForm()

    return render(request, 'apploan/modals/apply-renew-car.html', {'form': form})


def formMotor(request):
    if request.method == 'POST':
        form = ApplyCOEForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.vehicle_type = 'motor'
            instance.save()

            next_url = request.POST.get('next', '/')
            return redirect(f"{next_url}?submitted=true")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ApplyCOEForm()

    return render(request, 'apploan/modals/apply-renew-motor.html', {'form': form})

# About
def about(request):
    return render(request, 'apploan/about.html')

def apply(request):
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect with submitted flag for success modal
            next_url = request.POST.get('next', '/')
            return redirect(f"{next_url}?submitted=true")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ApplyForm()
    return render(request, 'apply.html', {'form': form})


def enquire(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect with submitted flag for success modal
            next_url = request.POST.get('next', '/')
            return redirect(f"{next_url}?submitted=true")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EnquiryForm()

    return render(request, 'enquire.html', {'form': form})

def mQuote(request):
    if request.method == "POST":
        form = QuoteMotorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{request.POST.get('next', '/')}?submitted=true")
    else:
        form = QuoteMotorForm()
    return render(request, "quote-m.html", {"form": form})

def cQuote(request): 
    if request.method == "POST":
        form = QuoteCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{request.POST.get('next', '/')}?submitted=true")
    else:
        form = QuoteCarForm()
    
    return render(request, "quote-c.html", {"form": form})

def contact(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # For now, just print to console (or save to DB later)
        print(f"{name}, {email}, {message}")
        return HttpResponse("Thank you for contacting us!")
    return render(request, 'apploan/contact.html')


