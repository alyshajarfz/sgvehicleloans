# apploan/context_processors.py
from .models import MenuSetting, LoanRate

def menu_setting(request):
    settings, created = MenuSetting.objects.get_or_create(id=1) 
    return {"menu_setting": settings}


def loan_rates(request):
    """
    Returns all loan rates as a dictionary keyed by loan_name.
    Example in template: loan_rates.used_cm
    """
    rates = {rate.loan_name: rate for rate in LoanRate.objects.all()}
    return {'loan_rates': rates}
