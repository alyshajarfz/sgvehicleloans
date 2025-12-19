from django import template

register = template.Library()

@register.simple_tag
def get_faqs(page):
    """Return FAQ list based on the page/category"""
    
    faqs = {
        "used": [
            {"question": "What are your eligibility criteria for used car loans?",
             "answer": "<ul><li>Singaporeans, Singapore PRs, Foreigners</li>"
                       "<li>Applicants should be between 21 – 65 years of age</li></ul>"},
            {"question": "How soon will I know if my used car loan application is approved?",
             "answer": "Approval usually takes 1-2 working days. Our finance expert will inform you via phone/email."},
            {"question": "How do I follow up on my used car loan application?",
             "answer": "Contact us at +65 1111 2200 or +65 1111 2222 for follow-ups."},
            {"question": "Will you do the transfer of car ownership for me?",
             "answer": "Yes, the transfer of car ownership is done at no charge."},
            {"question": "Is there an application fee for used car loans?",
             "answer": "At AutoMotoCredit, we do not charge any application fee for used car loans."},
            {"question": "How can I check the status of my loan application?",
             "answer": "You can follow up via phone, email, or by visiting the branch where you submitted your application."},
        ],

        "new": [
            {"question": "Can I get a loan from AutoMotoCredit if I buy a car from a car dealer?",
             "answer": "Yes, you can. However, please check first with your car dealer if you are allowed to source or secure a car loan from a different company."},
            {"question": "What will be the minimum downpayment if I were to buy a car?",
             "answer": "The minimum downpayment is 30% of the car’s purchase price if its OMV is $20,000 or less – otherwise, it would be 40%."},
            {"question": "Who is eligible for a new car loan?",
             "answer": "<ul><li>Singaporeans, Singapore PRs, and foreign workers</li>"
                       "<li>A stable income to support monthly repayments</li>"
                       "<li>Meeting the bank or financial institution’s credit requirements</li></ul>"},
            {"question": "Can I get a new car loan if I have bad credit?",
             "answer": "Yes. While approval may be more challenging with a poor credit history, AutoMotoCredit works with multiple banks and lenders to help you get approved."},
            {"question": "Can I repay my loan early?",
             "answer": "Yes. Most lenders allow early repayment, although some may charge a small penalty. Paying early can save you on interest over the loan term."},
            {"question": "Can foreigners apply for a new car or motorcycle loan?",
             "answer": "Yes, foreign applicants are eligible, subject to additional documentation requirements."},
        ],

        "direct": [
            {"question": "Who will find this Direct Buyer → Seller useful?",
             "answer": "Both car buyers and private sellers will benefit—buyers get tailored financing, and sellers enjoy a smoother resale process."},
            {"question": "Why should I engage with AutoMotoCredit?",
             "answer": "Buying a used car involves many steps. We verify rightful ownership, handle financing, and simplify the entire process, saving you time and ensuring peace of mind."},
            {"question": "What does the Direct Buyer → Seller include?",
             "answer": "<ul><li>Car loan application and processing</li>"
                       "<li>Verification of car ownership</li>"
                       "<li>Full administrative support for transfer of ownership</li>"
                       "<li>Neutral third-party witness for transactions</li>"
                       "<li>Assistance with monetary transactions</li></ul>"},
            {"question": "What documents are required to apply?",
             "answer": "<ul><li>Buyer’s income proof (NOA or last 3 months’ payslips)</li>"
                       "<li>Buyer’s ID & driving license (front and back)</li>"
                       "<li>Sales & Purchase Agreement</li>"
                       "<li>Seller’s ID and vehicle details (logbook/logcard/assets acknowledgement)</li></ul>"},
            {"question": "What is the minimum downpayment?",
             "answer": "<ul><li>30% of the car’s purchase price if OMV ≤ $20,000</li>"
                       "<li>40% if OMV > $20,000</li></ul>"},
            {"question": "What if the car is still under financing?",
             "answer": "You don’t need to pay off the outstanding loan immediately. We include free settlement assistance as part of the loan approval process."},
            {"question": "Do you offer consignment or buyer/seller matching services?",
             "answer": "Yes, please send an enquiry and we will assist you."},
            {"question": "Can I use this loan for dealer cars?",
             "answer": "Yes, but please check with the dealer first if third-party financing is allowed."},
        ],

        "coe_car_loan": [
             {"question": "What is a COE car loan?", 
             "answer": "A COE car loan is a financing option that covers the cost of a car’s Certificate of Entitlement (COE) and/or the vehicle itself, helping you spread payments over time instead of paying upfront."},
            {"question": "Can I get a loan from AutoMotoCredit if I buy a car from a car dealer?", 
             "answer": "Yes, you can. However, please check first with your car dealer if you are allowed to source for or secure a car loan from a different company."},
            {"question": "What documents are required for approval?", 
             "answer": "<ul><li>NRIC or passport</li>"
                        "<li>Proof of income (salary slips, bank statements)</li>"
                        "<li>Vehicle quotation or invoice</li>"
                        "<li>Bank statements (if required by lender)</li></ul>"},
            {"question": "How long does approval take?", 
             "answer": "Approval can take anywhere from 1 to 5 business days, depending on the lender and completeness of your documentation. Some specialized car financing companies offer same-day or next-day approvals."},
            {"question": "Can foreigners apply for a COE car loan?", 
             "answer": "Yes, but lenders may have additional requirements such as higher deposits, proof of employment, or valid long-term passes. Eligibility depends on the lender’s policies."},
        ],

        "coe_ref": [
             {"question": "Can I refinance my car if my car is no longer under any financing?", 
             "answer": "Yes, refinancing is available for cars that are fully owned with no existing loans."},
            {"question": "Can I refinance my car loan if I want to convert my car to drive for Grab?", 
             "answer": "Yes, AutoMotoCredit allows refinancing for cars you want to use for ride-hailing services like Grab."},
            {"question": "What is the interest rate for car refinancing?", 
             "answer": "The interest rate depends on factors such as car age, market value, car condition, loan amount, and loan period."},
            {"question": "Can I refinance my car loan without affecting my TDSR or housing loan eligibility?", 
             "answer": "Yes, refinancing with AutoMotoCredit can be structured so it does not impact your TDSR or housing loan."},
            {"question": "What types of refinancing does AutoMotoCredit offer?", 
             "answer": "<ul><li>Cash out</li>"
                        "<li>Lower your interest rate</li>"
                        "<li>Reduce your monthly payments</li>"
                        "<li>Drive for Grab</li></ul>"},
            {"question": "Can I refinance my car if I want to transfer ownership to another person?", 
             "answer": "Yes, refinancing is possible even if you plan to transfer your car ownership."},
        ],

        "in_house": [
            {"question": "What is an in-house car loan?", 
             "answer": "An in-house car loan is financing provided directly by the car dealer or financing company, rather than a bank. It offers faster approval, flexible terms, and tailored options for buyers."},
            {"question": "Who is eligible for an in-house car loan?", 
             "answer": "Most individuals with a stable income can qualify, even if they have limited credit history or do not meet strict bank requirements. Eligibility depends on income, employment, and the car being financed."},
            {"question": "What is the difference between bank car financing and an in-house car loan?", 
             "answer": "<strong>Bank Car Financing:</strong>"
                        "<ul><li>Provided by banks or financial institutions.</li>"
                        "<li>Usually requires a higher credit score and stricter eligibility criteria.</li>"
                        "<li>Interest rates may be lower, but approval can take longer.</li>"
                        "<li>Typically involves standard loan terms with less flexibility.</li></ul>"
                        "<strong>In-House Car Loan:</strong><ul>"
                        "<li>Provided directly by the car dealership or financing company.</li>"
                        "<li>Often easier and faster to approve, with more flexible requirements.</li>"
                        "<li>Can include options tailored to your needs, such as ride-hailing usage or buyout plans.</li>"
                        "<li>Interest rates may be slightly higher than bank loans, but the process is more convenient.</li></ul>"
                        "Summary: Bank loans focus on strict credit evaluation and standardized terms, while in-house loans prioritize faster, flexibility, and convenience."},
            {"question": "How long does it take to get approved for an in-house car loan?", 
             "answer": "Approval is typically much faster than bank loans, often within a few days, depending on documentation and car evaluation."},
            {"question": "Are there any disadvantages of an in-house car loan?", 
             "answer": "<ul><li>Interest rates may be slightly higher than banks</li>"
                        "<li>Loan terms may be shorter</li>"
                        "<li>Limited to cars financed or approved by the in-house provider</li></ul>"},
        ],

        "phv": [
            {"question": "Is inspection required for PHV?", 
             "answer": "Yes. With effect from 1 January 2021, inspection at any LTA-authorised inspection centre is required before conversion of scheme. Online conversion and PHV decals must be affixed within 3 calendar days."},
            {"question": "What are the conversion charges for the PHV scheme by LTA?", 
             "answer": "The conversion fee is $100 per vehicle."},
            {"question": "Why are interest rates for Grab Cars higher than a normal car loan?", 
             "answer": "PHV cars are on the road much more frequently than normal cars, leading to higher exposure to risks. Wear and tear occurs faster, reducing the vehicle’s residual value. Higher interest rates reflect these increased risks."},
            {"question": "Is the insurance for Grab cars different from normal cars?", 
             "answer": "Yes, insurance premiums and excess are higher for PHV vehicles due to increased risk exposure and faster depreciation."},
            {"question": "How soon will I know if my PHV car loan is approved?", 
             "answer": "Approval typically takes a few working days after submission. You will be notified once a decision is made."},
            {"question": "Are there restrictions on the type of car that can be used as a PHV?", 
             "answer": "Only vehicles approved by LTA for PHV use are eligible. Certain models or high-value vehicles may require additional approval."},
            {"question": "What documents are required for a PHV car loan?", 
             "answer": "<ul><li>Proof of identity (NRIC or passport)</li>"
                        "<li>Proof of income (salary slips or bank statements)</li>"
                        "<li>Vehicle details (invoice, insurance, registration documents)</li>"
                        "<li>PHV license or LTA conversion approval documents</li></ul>"},
            {"question": "Are there special terms for PHV car loans compared to regular car loans?", 
             "answer": "Yes, due to higher risk and faster depreciation, interest rates, insurance, and loan terms may differ from standard car loans."},
            {"question": "Can I use a used car as a PHV?", 
             "answer": "Yes, used cars can be converted for PHV use, provided they meet LTA’s age and safety requirements."},
        ],

        "coe_renew_car": [
            {"question": "Do I need to visit LTA to renew my COE?", 
             "answer": "No, there’s no need to go to LTA. We will handle your COE renewal and process all necessary LTA documents on your behalf."},
            {"question": "What are the interest rates and repayment periods?", 
             "answer": "Current interest rates start from 2.78% and may vary over time.<br>Repayment period depends on your COE renewal choice:<br>5-year COE renewal: 4 years repayment<br>10-year COE renewal: 7 years repayment"},
            {"question": "How long does loan approval take?", 
             "answer": "Instant in-principle approval: ~3 minutes<br>Non-instant approval: 1–3 working days"},
            {"question": "What payment modes are available for monthly instalments?", 
             "answer": "Bank transfer, PayNow, GIRO, cash, or cheque deposit"},
            {"question": "Can I apply for the loan if I’m not the car owner?", 
             "answer": "Yes, but the actual car owner must approve and sign all documents."},
            {"question": "When is the best time to submit my application?", 
             "answer": "Ideally, 4–6 weeks before your COE expiry date."},
            {"question": "Any difference between 5-year and 10-year COE renewal?", 
             "answer": "5-year renewal: Car must be deregistered after 5 years<br>10-year renewal: Car is eligible for a second COE renewal"},
            {"question": "Is it compulsory to renew my insurance with your company?", 
             "answer": "No, you are not required to renew your insurance with us."},
            {"question": "Can I do an early COE renewal?", 
             "answer": "Yes, but note that remaining PARF & COE rebate will be forfeited if you renew early.<br>Example: COE expiry: 15 April 2021, Early renewal in January 2021, COE renewed using January PQP, new expiry: 31 January 2031"},
            {"question": "Will you bid the COE for me?", 
             "answer": "No bidding is needed for COE renewal. We pay the Prevailing Quota Premium (PQP) for your vehicle category and handle the renewal."},
            {"question": "Can you renew an expired COE?", 
             "answer": "Yes, if the COE has expired within 1 month. Late renewal fees may apply."},
            {"question": "Are PQP rates different for OPC/ROPC and normal cars?", 
             "answer": "No, PQP is the same for OPC/ROPC and normal vehicles."},
            {"question": "What is the maximum financing amount?", 
             "answer": "We provide 100% financing based on PQP. Case-by-case exceptions for higher financing may apply at a higher interest rate."},
            {"question": "How much will my monthly instalment be?", 
             "answer": "Monthly instalments depend on PQP, interest rate, and loan tenure. We can provide a detailed quotation or an indicative figure using our Monthly Repayment Calculator."},
            {"question": "What documents are required?", 
             "answer": "<ul><li>Signed & completed loan application form</li>"
                        "<li>NRIC (front & back)</li><li>Income documents (any of the following): 2-year Notice of Assessment (NOA), Latest 12 months CPF contribution statement, 6 months computerized payslip, Latest 3 months bank statement (if self-employed)</li>"
                        "<li>Vehicle log card</li></ul>"},
            {"question": "How do I apply?", 
             "answer": "Submit an online application or enquiry form. Our car financing and COE experts will contact you, guide you through the process, and handle all paperwork."},
            {"question": "What is the procedure like?", 
             "answer": "Loan submission ➜ Loan approval ➜ Signing of agreement ➜ COE renewal"},
        ],

        "coe_renew_motor": [
            {"question": "Do I need to visit LTA to renew my motorcycle’s COE?", 
             "answer": "No, there’s no need to go to LTA. We will handle your COE renewal and process all necessary LTA documents for you."},
            {"question": "What is the interest rate and repayment period?", 
             "answer": "Special interest rate: 5.98% (subject to promotion period; contact us for the latest rates).<br>Repayment period depends on your COE renewal choice:<br>5-year COE renewal: 4 years repayment<br>10-year COE renewal: 7 years repayment"},
            {"question": "Is there an administrative fee?", 
             "answer": "Yes, there is a one-time admin fee for Motorcycle COE Renewal Loan."},
            {"question": "What is the maximum financing amount?", 
             "answer": "We provide 100% financing based on the PQP (Prevailing Quota Premium) amount."},
            {"question": "How much will my monthly instalment be?", 
             "answer": "Monthly instalments depend on PQP, interest rate, and loan tenure. We can provide a detailed quotation via email. For an indicative figure, you can use our Monthly Repayment Calculator."},
            {"question": "What documents are required to apply?", 
             "answer": "<ul><li>Completed loan application form</li><li>NRIC (front & back)</li>"
                        "<li>Income documents (any of the following): 2-year Notice of Assessment (NOA), Latest 12 months CPF contribution assessment, 6 months computerized payslip, Latest 3 months bank statement (if self-employed)</li><li>Vehicle log card</li></ul>"},
            {"question": "How do I apply for a Motorcycle COE Renewal Loan?", 
             "answer": "Submit an online application or enquiry form. Our experts will contact you, guide you through the process, and handle all paperwork."},
            {"question": "What is the procedure like?", 
             "answer": "Loan submission ➜ Loan approval ➜ Signing of agreement ➜ COE renewal"},
            {"question": "When is the best time to submit the application?", 
             "answer": "Ideally, 4–6 weeks before your motorcycle’s COE expiry date."},
            {"question": "Any difference between 5-year and 10-year COE renewal?", 
             "answer": "5-year COE renewal: Motorcycle must be deregistered at the end of 5 years<br>10-year COE renewal: Motorcycle is eligible for a second COE renewal"},
            {"question": "Can I submit my application via email or walk-in?", 
             "answer": "Either is acceptable, but we prefer online submission via our website or corporate email (credit@automoto.com.sg)."},
            {"question": "Can I do early COE renewal?", 
             "answer": "Yes, but LTA will forfeit the remaining PARF & COE rebate if renewed early.<br>Example: COE expiry: 15 April 2021, Early renewal in January 2021, New COE expiry: 31 January 2031"},
            {"question": "Will you bid the COE for me?", 
             "answer": "No bidding is required for COE renewal. We pay the Prevailing Quota Premium (PQP) for your motorcycle category and handle the renewal process."},
            {"question": "Can you renew an expired COE?", 
             "answer": "Yes, if the COE expired within 1 month. Late renewal fees may apply. More info: LTA COE Renewal"},
        ]
    }

    return faqs.get(page, [])
