from django import forms
from .models import QuoteMotor, QuoteCar, Enquiry, EnquiryRenew, Apply, ApplyCOE, InstallmentSubmit, Contact

class QuoteMotorForm(forms.ModelForm):
    # Generate year choices dynamically (2025 down to 1930)
    YEAR_CHOICES = [(str(year), str(year)) for year in range(2025, 1929, -1)]

    year_reg = forms.ChoiceField(
        choices=[('', '---------')] + YEAR_CHOICES,  # Placeholder at top
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = QuoteMotor
        fields = "__all__"
        widgets = {
            "brand": forms.Select(attrs={"class": "form-select"}),
            "model": forms.TextInput(attrs={"class": "form-control","placeholder": "Enter motorcycle model", 'required': True}),
            "name": forms.TextInput(attrs={"class": "form-control","placeholder": "Enter your full name", 'required': True}),
            "gender": forms.Select(attrs={"class": "form-select", 'required': True}),
            "status": forms.Select(attrs={"class": "form-select", 'required': True}),
            "number": forms.TextInput(attrs={"class": "form-control","placeholder": "Enter your mobile number", 'required': True}),
            "dob": forms.DateInput(attrs={"type": "date","class": "form-control", 'required': True}),
            "occupation": forms.Select(attrs={"class": "form-select", 'required': True}),
            "ride_exp": forms.Select(attrs={"class": "form-select", 'required': True}),
            "ncd_disc": forms.Select(attrs={"class": "form-select", 'required': True}),
            "licence": forms.Select(attrs={"class": "form-select", 'required': True}),
            "named_rider": forms.Select(attrs={"class": "form-select", 'required': True}),
            "claims": forms.Select(attrs={"class": "form-select", 'required': True}),
            "start_date": forms.DateInput(attrs={"type": "date","class": "form-control", 'required': True}),
            "end_date": forms.DateInput(attrs={"type": "date","class": "form-control", 'required': True}),
            "remarks": forms.Textarea(attrs={"class": "form-control","rows": 4, "placeholder": "Any additional remarks"}),
            "privacy_policy": forms.CheckboxInput(attrs={"class": "form-check-input", 'required': True}),
        }


class QuoteCarForm(forms.ModelForm):
    # Generate year choices dynamically (2025 down to 1930)
    YEAR_CHOICES = [(str(year), str(year)) for year in range(2025, 1929, -1)]

    year_reg = forms.ChoiceField(
        choices=[('', '---------')] + YEAR_CHOICES,  # Placeholder option
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = QuoteCar
        fields = "__all__"
        widgets = {
            "brand": forms.Select(attrs={"class": "form-select", 'required': True}),
            "model": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Car Model", 'required': True}),
            "scheme": forms.Select(attrs={"class": "form-select", 'required': True}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Full Name", 'required': True}),
            "gender": forms.Select(attrs={"class": "form-select", 'required': True}),
            "status": forms.Select(attrs={"class": "form-select", 'required': True}),
            "number": forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Mobile Number", 'required': True}),
            "dob": forms.DateInput(attrs={"type": "date", "class": "form-control", 'required': True}),
            "occupation": forms.Select(attrs={"class": "form-select", 'required': True}),
            "vec_number": forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Vehicle Number", 'required': True}),
            "ncd_disc": forms.Select(attrs={"class": "form-select", 'required': True}),
            "licence": forms.Select(attrs={"class": "form-select", 'required': True}),
            "driver": forms.Select(attrs={"class": "form-select", 'required': True}),
            "claims": forms.Select(attrs={"class": "form-select", 'required': True}),
            "start_date": forms.DateInput(attrs={"type": "date","class": "form-control", 'required': True}),
            "end_date": forms.DateInput(attrs={"type": "date","class": "form-control", 'required': True}),
            "remarks": forms.Textarea(attrs={"class": "form-control","rows": 4,"placeholder": "Any Remarks"}),
            "privacy_policy": forms.CheckboxInput(attrs={"class": "form-check-input", 'required': True}),
        }


class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'mobile', 'email', 'enquiry_type', 'privacy_policy']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': True}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'enquiry_type': forms.Select(attrs={'class': 'form-select', 'required': True}),
            "privacy_policy": forms.CheckboxInput(attrs={"class": "form-check-input", 'required': True}),
        }


class EnquiryRenewCarForm(forms.ModelForm):
    class Meta:
        model = EnquiryRenew
        fields = [
            'first_name', 'last_name', 'mobile', 'email',
            'loan_type', 'coe_category_type', 'is_phv', 'coe_renewal_period', 'privacy_policy'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': True}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'coe_category_type': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'is_phv': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'coe_renewal_period': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'privacy_policy': forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': True}),
            'loan_type': forms.HiddenInput(),
        }

class EnquiryRenewMotorcycleForm(forms.ModelForm):
    class Meta:
        model = EnquiryRenew
        fields = [
            'first_name', 'last_name', 'mobile', 'email',
            'loan_type', 'coe_renewal_period', 'privacy_policy'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': True}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'coe_renewal_period': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'privacy_policy': forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': True}),
            'loan_type': forms.HiddenInput(),
        }

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'required': True,"placeholder": "Enter Full Name"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': True,"placeholder": "Enter Phone Number"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True,"placeholder": "Enter Email Address"}),
            'car_source': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'vehicle_price': forms.NumberInput(attrs={'class': 'form-control', 'required': True,"placeholder": "Enter vehicle Price"}),
            'vehicle_model': forms.TextInput(attrs={'class': 'form-control', 'required': True,"placeholder": "Enter Vehicle Model"}),
            'omv': forms.NumberInput(attrs={'class': 'form-control', 'required': True,"placeholder": "Enter Open Market Value (OMV)"}),
            'arf': forms.NumberInput(attrs={'class': 'form-control', 'required': True,"placeholder": "Enter Additional Registration Fee (ARF)"}),
            'registration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control', 'required': True,"placeholder": "Enter Registration Number"}),
            'lta_access_code': forms.TextInput(attrs={'class': 'form-control', 'required': True,"placeholder": "Enter LTA Access Code"}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control', 'required': True,"placeholder": "Enter Amount"}),
            'loan_tenure': forms.NumberInput(attrs={'class': 'form-control', 'required': True,"placeholder": "Enter Tenure"}),
            'loan_type': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'repayment_mode': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'preferred_bank': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'down_payment': forms.NumberInput(attrs={'class': 'form-control',"placeholder": "Enter Down Payment"}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'required': True,"placeholder": "Enter Remarks Here..."}),
            'privacy_policy': forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': True}),
        }


class ApplyCOEForm(forms.ModelForm):
    class Meta:
        model = ApplyCOE
        fields = ['full_name', 'contact_number', 'email', 'consent']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Full Name','required': True}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Contact Number','required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email Address','required': True}),
            'consent': forms.CheckboxInput(attrs={'class': 'form-check-input','required': True}),
        }



class InstallmentSubmitForm(forms.ModelForm):
    class Meta:
        model = InstallmentSubmit
        fields = ['full_name', 'nric', 'contact', 'email', 'vehicle_reg','install_amount','transfer_amount','reference','proof_pay',
                'remarks','privacy_policy',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name', 'required': True}),
            'nric': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NRIC', 'required': True}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'vehicle_reg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Registration Number', 'required': True}),
            'install_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Installment Amount', 'required': True}),
            'transfer_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Transfer Amount', 'required': True}),
            'reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reference', 'required': True}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Remarks'}),
            'privacy_policy': forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': True}),
        }


from django import forms

class ContactForm(forms.ModelForm):
    captcha_answer = forms.IntegerField(
        label="CAPTCHA: 5 + 4 = ?", required=True,widget=forms.NumberInput(attrs={
            'class': 'form-control',  
            'placeholder': 'CAPTCHA: 5 + 4 = ?'
        })
    )

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'email', 'enquiry_type', 'message', 'privacy_policy', 'captcha_answer']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'enquiry_type': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your message'}),
            'privacy_policy': forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': True}),
        }

    def clean_captcha_answer(self):
        answer = self.cleaned_data.get('captcha_answer')
        if answer != 9:  # 5 + 4 = 9
            raise forms.ValidationError("Incorrect CAPTCHA answer.")
        return answer
