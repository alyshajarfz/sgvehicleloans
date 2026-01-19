# apploan/models.py
from django.db import models


# Navbar
class MenuSetting(models.Model):
    # Main menu toggles
    show_home = models.BooleanField(default=True, verbose_name="Show Home")
    show_financing = models.BooleanField(default=True, verbose_name="Show Financing")
    show_coe = models.BooleanField(default=True, verbose_name="Show COE")
    show_insurance = models.BooleanField(default=True, verbose_name="Show Insurance")
    show_rates = models.BooleanField(default=True, verbose_name="Show Rates")
    show_guides = models.BooleanField(default=True, verbose_name="Show Guides")
    show_about = models.BooleanField(default=True, verbose_name="Show About")
    show_contact = models.BooleanField(default=True, verbose_name="Show Contact")

    # Financing dropdown toggles
    finance_used = models.BooleanField(default=True, verbose_name="Used Cars")
    finance_new = models.BooleanField(default=True, verbose_name="New Cars")
    finance_direct = models.BooleanField(default=True, verbose_name="Direct Financing")
    finance_coe_car = models.BooleanField(default=True, verbose_name="COE Cars")
    finance_refinance = models.BooleanField(default=True, verbose_name="Refinance")
    finance_inhouse = models.BooleanField(default=True, verbose_name="In-House Financing")
    finance_phv = models.BooleanField(default=True, verbose_name="PHV Financing")

    # COE dropdown toggles
    coe_car = models.BooleanField(default=True, verbose_name="Car COE")
    coe_moto = models.BooleanField(default=True, verbose_name="Motorcycle COE")

    # Insurance dropdown toggles
    insurance_car = models.BooleanField(default=True, verbose_name="Car Insurance")
    insurance_motor = models.BooleanField(default=True, verbose_name="Motorcycle Insurance")

    # Guides dropdown toggles
    guides_calc = models.BooleanField(default=True, verbose_name="Calculator")
    guides_faq = models.BooleanField(default=True, verbose_name="FAQ")
    guides_install = models.BooleanField(default=True, verbose_name="Installment")
    guides_pay = models.BooleanField(default=True, verbose_name="Payment")

    def __str__(self):
        return "Navbar Menu"
    

# Loan Rates
class LoanRate(models.Model):
    loan_name = models.CharField(max_length=50)
    loan_display = models.CharField(max_length=100, blank=True, null=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    financing = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return self.loan_display or self.loan_name
    
# Quotation
class QuoteMotor(models.Model):

    # --- CHOICES ---

    BRAND_CHOICES = [
        ("Yamaha", "Yamaha"),
        ("Honda", "Honda"),
        ("Suzuki", "Suzuki"),
        ("Kawasaki", "Kawasaki"),
        ("KTM", "KTM"),
        ("Ducati", "Ducati"),
        ("Royal Enfield", "Royal Enfield"),
        ("BMW", "BMW Motorrad"),
        ("Triumph", "Triumph"),
        ("CFMOTO", "CFMOTO"),
        ("SYM", "SYM"),
        ("Kymco", "Kymco"),
        ("Aprilia", "Aprilia"),
        ("Benelli", "Benelli"),
        ("Moto Guzzi", "Moto Guzzi"),
        ("Bimota", "Bimota"),
        ("Husqvarna", "Husqvarna"),
        ("GasGas", "GasGas"),
        ("Indian", "Indian Motorcycle"),
        ("Harley-Davidson", "Harley-Davidson"),
        ("Zero", "Zero Motorcycles"),
    ]


    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    MARITAL_CHOICES = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorce", "Divorce"),
    ]

    OCCUPATION_CHOICES = [
        ("Manager", "Manager"),
        ("Engineer", "Engineer"),
        ("Driver", "Driver"),
        ("Technician", "Technician"),
        ("Teacher", "Teacher"),
        ("Nurse", "Nurse"),
        ("Doctor", "Doctor"),
        ("Accountant", "Accountant"),
        ("Administrator", "Administrator"),
        ("Salesperson", "Salesperson"),
        ("Customer Service", "Customer Service"),
        ("Supervisor", "Supervisor"),
        ("Chef", "Chef"),
        ("Cashier", "Cashier"),
        ("Security Officer", "Security Officer"),
        ("Cleaner", "Cleaner"),
        ("Construction Worker", "Construction Worker"),
        ("IT Specialist", "IT Specialist"),
        ("Software Developer", "Software Developer"),
        ("Designer", "Designer"),
        ("Marketing Executive", "Marketing Executive"),
        ("Human Resource", "Human Resource"),
        ("Electrician", "Electrician"),
        ("Plumber", "Plumber"),
        ("Mechanic", "Mechanic"),
        ("Logistics Coordinator", "Logistics Coordinator"),
        ("Warehouse Assistant", "Warehouse Assistant"),
        ("Delivery Rider", "Delivery Rider"),
        ("Waiter", "Waiter"),
        ("Barista", "Barista"),
        ("Business Owner", "Business Owner"),
        ("Self-Employed", "Self-Employed"),
        ("Unemployed", "Unemployed"),
        ("Student", "Student"),
        ("Housewife", "Housewife"),
        ("Retiree", "Retiree"),
        ("Others", "Others"),
    ]


    RIDING_EXP_CHOICES = [
        ("1 Year", "1 Year"),
        ("2 Years", "2 Years"),
        ("3 Years", "3 Years"),
        ("4 Years", "4 Years"),
        ("5+ Years", "5+ Years"),
    ]

    NCD_CHOICES = [
        ("0%", "0%"),
        ("10%", "10%"),
        ("20%", "20%"),
        ("30%", "30%"),
    ]

    LICENCE_CHOICES = [
        ("1 Year", "1 Year"),
        ("2 Years", "2 Years"),
        ("3 Years", "3 Years"),
        ("4 Years", "4 Years"),
        ("5+ Years", "5+ Years"),
    ]

    RIDER_CHOICES = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
    ]

    CLAIM_CHOICES = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4+", "4+"),
    ]

    # --- MODEL FIELDS ---

    brand = models.CharField(max_length=100, choices=BRAND_CHOICES)
    model = models.CharField(max_length=255)
    year_reg = models.CharField(max_length=20)

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    status = models.CharField(max_length=10, choices=MARITAL_CHOICES)
    number = models.CharField(max_length=20)
    dob = models.DateField()
    occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES)

    ride_exp = models.CharField(max_length=50, choices=RIDING_EXP_CHOICES)
    ncd_disc = models.CharField(max_length=10, choices=NCD_CHOICES)
    licence = models.CharField(max_length=50, choices=LICENCE_CHOICES)
    named_rider = models.CharField(max_length=10, choices=RIDER_CHOICES)
    claims = models.CharField(max_length=10, choices=CLAIM_CHOICES)

    start_date = models.DateField()
    end_date = models.DateField()
    remarks = models.TextField(blank=True)

    privacy_policy = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    

    from django.db import models

class QuoteCar(models.Model): 
    # --- CHOICES ---
    BRAND_CHOICES = [
        ("Honda", "Honda"),
        ("BMW", "BMW"),
        ("Toyota", "Toyota"),
        ("Mercedes-Benz", "Mercedes-Benz"),
        ("Audi", "Audi"),
        ("Volkswagen", "Volkswagen"),
        ("Nissan", "Nissan"),
        ("Mazda", "Mazda"),
        ("Hyundai", "Hyundai"),
        ("Kia", "Kia"),
        ("Subaru", "Subaru"),
        ("Volvo", "Volvo"),
        ("Mitsubishi", "Mitsubishi"),
        ("Ford", "Ford"),
        ("Lexus", "Lexus"),
        ("Porsche", "Porsche"),
        ("Jaguar", "Jaguar"),
        ("Land Rover", "Land Rover"),
        ("Chevrolet", "Chevrolet"),
        ("Peugeot", "Peugeot"),
        ("Renault", "Renault"),
        ("Ferrari", "Ferrari"),
        ("Lamborghini", "Lamborghini"),
        ("Maserati", "Maserati"),
        ("Bentley", "Bentley"),
        ("Rolls-Royce", "Rolls-Royce"),
        ("McLaren", "McLaren"),
        ("Bugatti", "Bugatti"),
        ("Tesla", "Tesla"),
        ("Infiniti", "Infiniti"),
        ("Acura", "Acura"),
        ("Mini", "Mini"),
        ("Suzuki", "Suzuki"),
        ("Isuzu", "Isuzu"),
        ("Citroen", "Citroen"),
        ("Alfa Romeo", "Alfa Romeo"),
        ("Jaguar", "Jaguar"),
        ("Jeep", "Jeep"),
        ("Chrysler", "Chrysler"),
        ("Daihatsu", "Daihatsu"),
    ]


    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    MARITAL_CHOICES = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorce", "Divorce"),
    ]

    OCCUPATION_CHOICES = [
        ("Manager", "Manager"),
        ("Engineer", "Engineer"),
        ("Driver", "Driver"),
        ("Technician", "Technician"),
        ("Teacher", "Teacher"),
        ("Nurse", "Nurse"),
        ("Doctor", "Doctor"),
        ("Accountant", "Accountant"),
        ("Administrator", "Administrator"),
        ("Salesperson", "Salesperson"),
        ("Customer Service", "Customer Service"),
        ("Supervisor", "Supervisor"),
        ("Chef", "Chef"),
        ("Cashier", "Cashier"),
        ("Security Officer", "Security Officer"),
        ("Cleaner", "Cleaner"),
        ("Construction Worker", "Construction Worker"),
        ("IT Specialist", "IT Specialist"),
        ("Software Developer", "Software Developer"),
        ("Designer", "Designer"),
        ("Marketing Executive", "Marketing Executive"),
        ("Human Resource", "Human Resource"),
        ("Electrician", "Electrician"),
        ("Plumber", "Plumber"),
        ("Mechanic", "Mechanic"),
        ("Logistics Coordinator", "Logistics Coordinator"),
        ("Warehouse Assistant", "Warehouse Assistant"),
        ("Delivery Rider", "Delivery Rider"),
        ("Waiter", "Waiter"),
        ("Barista", "Barista"),
        ("Business Owner", "Business Owner"),
        ("Self-Employed", "Self-Employed"),
        ("Unemployed", "Unemployed"),
        ("Student", "Student"),
        ("Housewife", "Housewife"),
        ("Retiree", "Retiree"),
        ("Others", "Others"),
    ]

    NCD_CHOICES = [
        ("0%", "0%"),
        ("10%", "10%"),
        ("20%", "20%"),
        ("30%", "30%"),
    ]

    LICENCE_CHOICES = [
        ("1 Year", "1 Year"),
        ("2 Years", "2 Years"),
        ("3 Years", "3 Years"),
        ("4 Years", "4 Years"),
        ("5+ Years", "5+ Years"),
    ]

    CLAIM_CHOICES = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4+", "4+"),
    ]

    SCHEME_CHOICES = [
        ("Off-peak", "Off-peak"),
        ("Non off-peak", "Non off-peak"),
    ]

    DRIVER_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]

    # --- MODEL FIELDS ---
    brand = models.CharField(max_length=100, choices=BRAND_CHOICES)
    model = models.CharField(max_length=255)
    year_reg = models.CharField(max_length=20)
    scheme = models.CharField(max_length=50, choices=SCHEME_CHOICES)

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    status = models.CharField(max_length=10, choices=MARITAL_CHOICES)
    number = models.CharField(max_length=20)
    dob = models.DateField()
    occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES)

    vec_number = models.CharField(max_length=50)
    ncd_disc = models.CharField(max_length=10, choices=NCD_CHOICES)
    licence = models.CharField(max_length=50, choices=LICENCE_CHOICES)
    driver = models.CharField(max_length=10, choices=DRIVER_CHOICES)
    claims = models.CharField(max_length=10, choices=CLAIM_CHOICES)

    start_date = models.DateField()
    end_date = models.DateField()
    remarks = models.TextField(blank=True)

    privacy_policy = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


# Header Media
class HeaderVideo(models.Model):
    INS_CHOICES = [
        ('car', 'Car Insurance'),
        ('motorcycle', 'Motorcycle Insurance'),
    ]

    insurance_type = models.CharField(max_length=20, choices=INS_CHOICES, unique=True)
    video = models.FileField(upload_to='header_videos/', help_text="Maximum file size: 20 MB. Please Trim or Compress on (https://www.freeconvert.com/video-compressor) before uploading.")

    def __str__(self):
        return f"{self.get_insurance_type_display()} Video"
    
class HeaderImage(models.Model):
    TEMP_CHOICES = [
        ('used_cm', 'Used Car & Motorcycle'),
        ('new_cm', 'New Car & Motorcycle'),
        ('direct_bs', 'Direct Buyer - Seller'),
        ('coe_car', 'COE Car'),
        # Add other modules
    ]
    
    template_type = models.CharField(max_length=50, choices=TEMP_CHOICES, unique=True)
    image = models.ImageField(upload_to='header_images/', help_text="Supported formats: PNG, JPG. Maximum upload size: 20 MB.")

    def __str__(self):
        return f"{self.get_template_type_display()} Image"
    

# Enquiry Models
class Enquiry(models.Model):
    ENQUIRY_CHOICES = [
        ('used_cm', 'Used Car & Motorcycle'),
        ('new_cm', 'New Car & Motorcycle'),
        ('direct_bs', 'Direct Buyer - Seller'),
        ('coe_car', 'COE Car'),
        # Add more 
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50)
    email = models.EmailField()
    enquiry_type = models.CharField(max_length=50, choices=ENQUIRY_CHOICES, default='used_cm',)
    privacy_policy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email}) - {self.get_enquiry_type_display()}"
    
class GeneralEnquiry(Enquiry):  # proxy model
    class Meta:
        proxy = True
        verbose_name = "General Enquiry"
        verbose_name_plural = "General Enquiries"

class EnquiryRenew(models.Model):
    LOAN_TYPE_CHOICES = [
        ('car', 'Car'),
        ('motorcycle', 'Motorcycle'),
    ]

    COE_CATEGORY_CHOICES = [
        ('Category A', 'Category A (Cars up To 1,600cc)'),
        ('Category B', 'Category B (Cars Above 1,600cc)'),
        ('Category C', 'Category C (Goods Vehicles & Buses)'),
    ]

    COE_RENEWAL_CHOICES = [
        ('5-Year Renewal', '5-Year Renewal'),
        ('10-Year Renewal', '10-Year Renewal'),
    ]

    PHV_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPE_CHOICES)
    
    # Car-specific fields
    coe_category_type = models.CharField(max_length=50, choices=COE_CATEGORY_CHOICES, blank=True, null=True)
    is_phv = models.CharField(max_length=3, choices=PHV_CHOICES, blank=True, null=True)

    # Common fields
    coe_renewal_period = models.CharField(max_length=20, choices=COE_RENEWAL_CHOICES)
    privacy_policy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.loan_type})"

class CarEnquiry(EnquiryRenew):
    class Meta:
        proxy = True
        verbose_name = 'Enquiry COE Renew Car'
        verbose_name_plural = 'Enquiries COE Renew Car'


class MotorcycleEnquiry(EnquiryRenew):
    class Meta:
        proxy = True
        verbose_name = 'Enquiry COE Renew Motorcycle'
        verbose_name_plural = 'Enquiries COE Renew Motorcycle'


# Application Models
class Apply(models.Model):
    LOAN_TYPE_CHOICES = [
        ('used_car', 'Used Car Loan'),
        ('new_car', 'New Car Loan'),
        ('coe_car', 'COE Car Loan'),
        ('direct_buyer', 'Direct Buyer → Seller Loan'),
    ]

    BANK_CHOICES = [
        ('maybank', 'Maybank'),
        ('uob', 'UOB'),
        ('dbs', 'DBS/POSB'),
        ('ocbc', 'OCBC'),
        ('hlf', 'Hong Leong Finance'),
        ('others', 'Others'),
    ]

    CAR_SOURCE_CHOICES = [
        ('direct_owner', 'Direct Owner'),
        ('car_dealer', 'Car Dealer'),
    ]
    
    REPAYMENT_CHOICES = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
    ]

    # STEP 1: Contact
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    # STEP 2: Vehicle
    car_source = models.CharField(max_length=50, choices=CAR_SOURCE_CHOICES)
    vehicle_price = models.DecimalField(max_digits=12, decimal_places=2)
    vehicle_model = models.CharField(max_length=100)
    omv = models.DecimalField(max_digits=10, decimal_places=2)
    arf = models.DecimalField(max_digits=10, decimal_places=2)
    registration_date = models.DateField()
    registration_number = models.CharField(max_length=50)
    lta_access_code = models.CharField(max_length=50)

    # STEP 3: Loan
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    loan_tenure = models.PositiveIntegerField()
    loan_type = models.CharField(max_length=50, choices=LOAN_TYPE_CHOICES)
    repayment_mode = models.CharField(max_length=20, choices=REPAYMENT_CHOICES)
    preferred_bank = models.CharField(max_length=50, choices=BANK_CHOICES)
    down_payment = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    # STEP 4: Remarks
    remarks = models.TextField()
    privacy_policy = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.loan_type}"

class Application(Apply):  # proxy model
    class Meta:
        proxy = True
        verbose_name = "General Applications"
        verbose_name_plural = "General Applications"

    
class ApplyCOE(models.Model):
    VEHICLE_TYPE_CHOICES = (
        ('car', 'Car'),
        ('motor', 'Motorcycle'),
    )

    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICES)
    full_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    consent = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.vehicle_type})"


class CarCOE(ApplyCOE):
    class Meta:
        proxy = True
        verbose_name = "Application COE Renewal Car"
        verbose_name_plural = "Application COE Renewal Car"


class MotorCOE(ApplyCOE):
    class Meta:
        proxy = True
        verbose_name = "Application COE Renewal Motorcycle"
        verbose_name_plural = "Application COE Renewal Motorcycle"


# Footer S
class FooterSetting(models.Model):
    address = models.TextField(default="400 Balestier Road,\nBalestier Plaza #02-23,\nSingapore 329802")
    google_map_embed = models.TextField(
        default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.750498216391!2d103.8478215758166!3d1.3256235616514813!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31da19d8ad2a9e11%3A0x1b8c2cdaf63e0fbb!2sBalestier%20Plaza!5e0!3m2!1sen!2smy!4v1764923928289!5m2!1sen!2smy"
    )
    
    # Contact info
    hotline = models.CharField(max_length=50, default="(+65) 6444 4400")
    office = models.CharField(max_length=50, default="+65 6681 6778")
    fax = models.CharField(max_length=50, default="+65 6256 1229")
    
    # Operating hours
    op_hours_weekdays = models.CharField(max_length=100, default="Mon–Fri: 10am–6pm")
    op_hours_sat = models.CharField(max_length=100, default="Sat: 12pm–4pm")
    
    # Social media
    facebook_url = models.URLField(default="https://www.facebook.com/login", help_text="Please put your Facebook page link here.")
    instagram_url = models.URLField(default="https://www.instagram.com/accounts/login/", blank=True, help_text="Please put your Instagram profile link here.")
    whatsapp_url = models.URLField(default="https://api.whatsapp.com/send?phone=6589259233&text=Hi%2C%20SGVehicleLoans", blank=True, help_text="Please put your WhatsApp link here.")
    tiktok_url = models.URLField(default="https://www.tiktok.com/login", blank=True, help_text="Please put your TikTok profile link here.")
    
    class Meta:
        verbose_name = "Footer Setting"
        verbose_name_plural = "Footer Settings"

    def __str__(self):
        return "Footer Settings"


# Installment
class InstallmentSubmit(models.Model):
    full_name = models.CharField(max_length=255)
    nric = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    email = models.EmailField()

    vehicle_reg = models.CharField(max_length=20)
    install_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monthly instalment amount")
    transfer_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount transferred")

    reference = models.CharField(max_length=100)
    proof_pay = models.FileField(upload_to='installments/', help_text="Upload transfer receipt")
    remarks = models.TextField(blank=True, null=True)

    privacy_policy = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.vehicle_reg}"
    
# Contact
class Contact(models.Model):
    ENQUIRY_CHOICES = [
        ('Car Loan', 'Car Loan'),
        ('Motorcycle Loan', 'Motorcycle Loan'),
        ('Insurance', 'Insurance'),
        ('Other', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    enquiry_type = models.CharField(max_length=50, choices=ENQUIRY_CHOICES)
    message = models.TextField(blank=True, null=True)
    privacy_policy = models.BooleanField(default=False)
    captcha = models.CharField(max_length=10, help_text="Simple math captcha")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.enquiry_type}"
