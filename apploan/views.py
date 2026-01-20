import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HeaderVideo, HeaderImage, FooterSetting, Application, CarCOE, MotorCOE, GeneralEnquiry, CarEnquiry, MotorcycleEnquiry, QuoteCar, QuoteMotor
from django.contrib import messages
from .forms import QuoteMotorForm, QuoteCarForm, EnquiryForm, EnquiryRenewCarForm, EnquiryRenewMotorcycleForm, ApplyForm, ApplyCOEForm, InstallmentSubmitForm, ContactForm
from datetime import datetime

from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Count

def dashboard_callback(request, context):

    recent_submissions_queryset = Application.objects.order_by('-created_at')  # latest first

    # Applications Chart
    applications_trend = {
        "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "data": [5, 7, 6, 8, 10, 12, 9] # Example data
    }

    # Last 2 weeks
    two_weeks_ago = now() - timedelta(days=14)

    LOAN_TYPE_DISPLAY = dict(Application.LOAN_TYPE_CHOICES)

    # Most trending loan types in the last 2 weeks
    trending_loans = (
        Application.objects.filter(created_at__gte=two_weeks_ago)
        .values('loan_type')
        .annotate(total=Count('id'))
        .order_by('-total')[:3]
    )

    for loan in trending_loans:
        loan['loan_type_display'] = LOAN_TYPE_DISPLAY[loan['loan_type']]

    # Update context for dashboard
    context.update({
        # Users
        "users_total": User.objects.count(),
        "users_today": User.objects.filter(date_joined__date=now().date()).count(),

        "custom_variable": "Hello from callback",

        # Applications trend
        "applications_trend": applications_trend,

        # Latest submissions
        "recent_submissions": recent_submissions_queryset[:10],

        # APPLICATIONS
        "app_general_total": Application.objects.count(),
        "app_coe_car_total": CarCOE.objects.count(),
        "app_coe_motor_total": MotorCOE.objects.count(),

        # ENQUIRIES
        "enquiry_general_total": GeneralEnquiry.objects.count(),
        "enquiry_coe_car_total": CarEnquiry.objects.count(),
        "enquiry_coe_motor_total": MotorcycleEnquiry.objects.count(),

        # QUOTES
        "quote_car_total": QuoteCar.objects.count(),
        "quote_motor_total": QuoteMotor.objects.count(),

        # TRENDING LOANS
        "trending_loans": trending_loans,
    })

    return context


def home(request):
    apply_form = ApplyForm()
    context = {
        'title': 'Car & Motorcycle Loan Singapore | Fast Approval | SGVehicleLoans',
        'description': 'Apply for car and motorcycle loans in Singapore with fast approval. Low interest hire purchase, refinancing, and flexible repayment options. Get a free quote today.',
        'apply_form': apply_form,
    }
    return render(request, 'apploan/home.html', context)

def financeUsed(request):
    header_image = HeaderImage.objects.filter(template_type='used_cm').first()
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'title': 'Used Car & Motorcycle Loan Singapore | Fast Approval | SGVehicleLoans',
        'description': 'Get used car and motorcycle financing in Singapore with fast approval. Flexible hire purchase plans, refinancing options, and competitive rates. Request a free quote today.',
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
        'title': 'Direct Car & Motorcycle Loan Singapore | Fast Approval | SG Vehicle Loans',
        'description': 'Get direct car and motorcycle financing in Singapore with fast approval. Low interest hire purchase options, flexible repayment plans, and quick quotations. Apply today.',
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
        'title': 'New Car & Motorcycle Loan Singapore | Fast Approval | SGVehicleLoans',
        'description': 'Apply for new car and motorcycle loans in Singapore with fast approval. Low interest hire purchase packages, flexible repayment plans, and quick quotations. Get a free quote today.',
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
        'title': 'COE Car Loan Singapore | COE Renewal Financing | Fast Approval',
        'description': 'Need COE car financing in Singapore? Get COE renewal loan options with fast approval support, flexible instalment plans, and competitive rates. Request a free quote today.',
        'header_image': header_image,
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }
    return render(request, 'apploan/financing/coe-car-loan.html', context)

def financeRefinance(request):
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'title': 'Car & Motorcycle Loan Refinancing Singapore | Lower Instalments Fast',
        'description': 'Refinance your car or motorcycle loan in Singapore to lower monthly instalments or get better rates. Fast approval support, flexible plans, and quick quotation. Apply now.',
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }
    
    return render(request, 'apploan/financing/car-refinancing.html', context)

def financeInHouse(request):
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'title': 'In-House Car & Motorcycle Loan Singapore | Fast Approval | SGVehicleLoans',
        'description': 'Get in-house car and motorcycle financing in Singapore with fast approval support. Flexible instalment plans, competitive rates, and quick quotation. Apply online today.',
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }
    
    return render(request, 'apploan/financing/in-house.html', context)


def financePHVCar(request):
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'title': 'PHV Car Loan Singapore | Grab & Private Hire Financing | Fast Approval',
        'description': 'Apply for PHV car loans in Singapore with fast approval support. Financing options for Grab and private hire vehicles, flexible instalments, and competitive rates. Get a free quote today.',
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }
    
    return render(request, 'apploan/financing/phv-car-loan.html', context)


# Insurance
def insCar(request):
    video = HeaderVideo.objects.filter(insurance_type='car').first()
    form = QuoteCarForm()
    enquiry_form = EnquiryForm()

    context = {
        'title': 'Car Insurance Singapore | Fast Quote & Competitive Rates | SGVehicleLoans',
        'description': 'Get car insurance in Singapore with fast quotation support. Competitive rates, flexible coverage options, and easy renewal. Request a free quote today.',
        'video': video,
        'form': form,
        'enquiry_form': enquiry_form,
    }

    return render(request, 'apploan/insurance/ins-car.html', context)


def insMotor(request):
    video = HeaderVideo.objects.filter(insurance_type='motorcycle').first()
    form = QuoteMotorForm()
    enquiry_form = EnquiryForm()

    context = {
        'title': 'Motorcycle Insurance Singapore | Fast Quote & Competitive Rates',
        'description': 'Get motorcycle insurance in Singapore with fast quotation support. Competitive rates, flexible coverage options, and easy renewal. Request a free quote today.',
        'video': video,
        'form': form,
        'enquiry_form': enquiry_form,
    }

    return render(request, 'apploan/insurance/ins-motor.html', context)


# Rates
def rates(request):
    apply_form = ApplyForm()
    enquiry_form = EnquiryForm()

    context = {
        'title': 'Car & Motorcycle Loan Interest Rates Singapore | Updated Financing Rates',
        'description': 'View car and motorcycle loan interest rates in Singapore. Compare hire purchase, refinancing, COE renewal financing rates, and flexible repayment options. Get a free quote today.',
        'apply_form': apply_form,
        'enquiry_form': enquiry_form,
    }

    return render(request, 'apploan/rates.html', context)


# Guides
def guidesCalc(request):
    context = {
        'title': 'Car & Motorcycle Loan Calculator Singapore | Instalment Guide & Rates',
        'description': 'Use our car and motorcycle loan calculator in Singapore to estimate monthly instalments. Learn about interest rates, hire purchase terms, and financing options. Calculate now.',
    }
    return render(request, 'apploan/guides/loan-calc.html', context)


def guidesFaq(request):
    context = {
        'title': 'Vehicle Loan FAQ Singapore | Car & Motorcycle Financing Guide | SGVL',
        'description': 'Find answers to common vehicle loan questions in Singapore. Learn about car and motorcycle loans, hire purchase, refinancing, COE renewal financing, and approvals. Read our FAQ guide.',
    }
    return render(request, 'apploan/guides/loan-faq.html', context)


def guidesInstall(request):
    if request.method == 'POST':
        form = InstallmentSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/?submitted=true')
        else:
            print(form.errors)
            messages.error(request, "Please correct the errors below.")
    else:
        form = InstallmentSubmitForm()

    context = {
        'title': 'Car & Motorcycle Loan Instalment Guide Singapore | Monthly Repayment Help',
        'description': 'Learn how car and motorcycle loan instalments work in Singapore. Understand monthly repayments, interest rates, tenure, and hire purchase terms. Use our guide to plan better.',
        'form': form,
    }
    return render(request, 'apploan/guides/loan-installment.html', context)


def guidesPay(request):
    context = {
        'title': 'Vehicle Loan Payment Guide Singapore | Car & Motorcycle Hire Purchase Tips',
        'description': 'Learn how vehicle loan payments work in Singapore. Understand car and motorcycle hire purchase payments, instalment schedules, fees, and early settlement options. Read the guide now.',
    }
    return render(request, 'apploan/guides/loan-pay.html', context)

# About
def about(request):
    context = {
        'title': 'About SG Vehicle Loans | Car & Motorcycle Financing Singapore',
        'description': 'SG Vehicle Loans helps drivers in Singapore get car and motorcycle financing with fast approval support. Explore our loan solutions including hire purchase, refinancing, and COE renewal financing.',
    }
    return render(request, 'apploan/about.html', context)

# Contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us!")
            return redirect(request.path)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    context = {
        'title': 'Contact SGVehicleLoans | Car & Motorcycle Loan Quote Singapore',
        'description': 'Contact SGVehicleLoans for car and motorcycle financing in Singapore.',
        'form': form,
    }
    return render(request, 'apploan/contact.html', context)


# Apply
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

# COE Renewal
def COERenewCar(request):
    if request.method == "POST":
        form = EnquiryRenewCarForm(request.POST, initial={'loan_type': 'car'})
        if form.is_valid():
            form.save()
            messages.success(request, "COE renewal application submitted successfully!")
            return redirect(request.path)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EnquiryRenewCarForm(initial={'loan_type': 'car'})

    context = {
        "form": form,
        "loan_type": "car",
        "title": "COE Renewal Car Singapore | COE Renewal Loan & Financing | Fast Approval",
        "description": "Renew your car COE in Singapore with flexible COE renewal financing. Fast approval support, competitive rates, and easy instalment plans. Request a free quote today.",
    }
    return render(request, "apploan/coe/coe-renew-car.html", context)


def COERenewMoto(request):
    if request.method == "POST":
        form = EnquiryRenewMotorcycleForm(request.POST, initial={'loan_type': 'motorcycle'})
        if form.is_valid():
            form.save()
            messages.success(request, "Motorcycle COE renewal submitted successfully!")
            return redirect(request.path)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EnquiryRenewMotorcycleForm(initial={'loan_type': 'motorcycle'})

    context = {
        "form": form,
        "loan_type": "motorcycle",
        "title": "Motorcycle COE Renewal Singapore | COE Renewal Loan & Financing Fast",
        "description": "Renew your motorcycle COE in Singapore with flexible COE renewal financing. Fast approval support, easy instalment plans, and competitive rates. Get a free quote today.",
    }
    return render(request, "apploan/coe/coe-renew-motor.html", context)


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


def footerSettings(request):
    footer = FooterSetting.objects.first()
    return {"footer": footer}
