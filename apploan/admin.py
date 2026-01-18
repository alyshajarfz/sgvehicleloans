from django.contrib import admin
from django import forms
from unfold.admin import ModelAdmin 
from .models import MenuSetting, LoanRate, Enquiry, QuoteMotor, QuoteCar, HeaderVideo, HeaderImage, CarEnquiry, MotorcycleEnquiry, Application, CarCOE, MotorCOE, FooterSetting

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(HeaderVideo)
class HeaderVideoAdmin(ModelAdmin):
    list_display = ('insurance_type', 'video')

@admin.register(HeaderImage)
class HeaderImageAdmin(ModelAdmin):
    list_display = ('template_type', 'image')


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined']

@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass

class MenuSettingForm(forms.ModelForm):
    class Meta:
        model = MenuSetting
        fields = '__all__'
        labels = {
            'show_home': 'Home',
            'show_financing': 'Financing',
            'show_coe':'COE Car Loan',
            'show_insurance':'Car Insurance',
            'show_rates': 'Rates',
            'show_guides':'Guides',
            'show_about':'About',
            'show_contact': 'Contact',
            'finance_used': 'Used Car & Motorcycle Loan',
            'finance_new': 'New Car & Motorcycle Loan',
            'finance_direct':'Direct Buyer → Seller Auto Loan',
            # Add all other fields here...
        }

# MenuSetting
@admin.register(MenuSetting)
class MenuSettingAdmin(ModelAdmin):
    form = MenuSettingForm
    fieldsets = (
        ("Main Menu", {
            "fields": ("show_home", "show_financing", "show_coe", "show_insurance",
                       "show_rates", "show_guides", "show_about", "show_contact")
        }),
        ("Financing Dropdown", {
            "fields": ("finance_used", "finance_new", "finance_direct", "finance_coe_car",
                       "finance_refinance", "finance_inhouse", "finance_phv")
        }),
        ("COE Dropdown", {
            "fields": ("coe_car", "coe_moto")
        }),
        ("Insurance Dropdown", {
            "fields": ("insurance_car", "insurance_motor")
        }),

        ("Guides Dropdown", {
            "fields": ("guides_calc", "guides_faq", "guides_install", "guides_pay")
        }),
    )

# LoanRate
@admin.register(LoanRate)
class LoanRateAdmin(ModelAdmin):
    foldable_fields = '__all__'
    list_display = ('loan_display', 'interest_rate', 'financing')
    list_editable = ('interest_rate', 'financing')
    list_display_links = ('loan_display',)

    exclude = ('loan_name',)

    def loan_display(self, obj):
        return obj.loan_display or obj.loan_name
    loan_display.short_description = 'Loan Name'

# Application
@admin.register(Application)
class ApplicationAdmin(ModelAdmin):
    list_display = ('full_name', 'loan_type', 'preferred_bank', 'created_at')
    list_filter = ('loan_type', 'preferred_bank', 'car_source', 'repayment_mode')
    search_fields = ('full_name', 'email', 'phone', 'registration_number')
    ordering = ('-created_at',)


# Enquiry
@admin.register(Enquiry)
class EnquiryAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'mobile')
    ordering = ('-created_at',)


@admin.register(QuoteMotor)
class QuoteMotorAdmin(ModelAdmin):
    # Columns to display in admin list view
    list_display = ('name', 'number', 'brand', 'model', 'created_at')
    
    # Fields to search in admin
    search_fields = ('name', 'number', 'brand', 'model')
    
    # Default ordering
    ordering = ('-created_at',)

@admin.register(QuoteCar)
class QuoteCarAdmin(ModelAdmin):
    list_display = ('name', 'number', 'brand', 'model', 'created_at')
    search_fields = ('name', 'number', 'brand', 'model')
    ordering = ('-created_at',)


@admin.register(CarEnquiry)
class CarEnquiryAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'coe_category_type', 'is_phv', 'coe_renewal_period', 'created_at')
    list_filter = ('coe_category_type', 'coe_renewal_period', 'is_phv')
    search_fields = ('first_name', 'last_name', 'mobile', 'email')
    ordering = ('-created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(loan_type='car')  # ONLY show cars


@admin.register(MotorcycleEnquiry)
class MotorcycleEnquiryAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'coe_renewal_period', 'created_at')
    list_filter = ('coe_renewal_period',)
    search_fields = ('first_name', 'last_name', 'mobile', 'email')
    ordering = ('-created_at',)

    exclude = ('is_phv', 'coe_category_type')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(loan_type='motorcycle')  # ONLY show motorcycles
    

@admin.register(CarCOE)
class CarCOEAdmin(ModelAdmin):
    list_display = ('full_name', 'contact_number', 'email', 'created_at')
    search_fields = ('full_name', 'email')
    list_filter = ('created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(vehicle_type='car')


@admin.register(MotorCOE)
class MotorCOEAdmin(ModelAdmin):
    list_display = ('full_name', 'contact_number', 'email', 'created_at')
    search_fields = ('full_name', 'email')
    list_filter = ('created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(vehicle_type='motor')
    
@admin.register(FooterSetting)
class FooterSettingAdmin(ModelAdmin):
    list_display = ('address', 'hotline', 'office', 'fax')
    
    fieldsets = (
        ("Company Info", {
            "fields": ("address", "google_map_embed")
        }),
        ("Contact Info", {
            "fields": ("hotline", "office", "fax")
        }),
        ("Operating Hours", {
            "fields": ("op_hours_weekdays", "op_hours_sat")
        }),
        ("Social Media", {
            "fields": ("facebook_url", "instagram_url", "whatsapp_url", "tiktok_url")
        }),
    )

    # Only allow one row
    def has_add_permission(self, request):
        return not FooterSetting.objects.exists()
