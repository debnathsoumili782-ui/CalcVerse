from django.shortcuts import render
from django.shortcuts import render


def home(request):
    return render(request, 'calculators/home.html')

def age_date_time(request):
    return render(
        request,
        "calculators/age-date-time/age-date-time.html"
    )
def age_calculator(request):
    return render(
        request,
        "calculators/age-date-time/age-calculator.html"
    )

def category(request, category_name):
    return render(
        request,
        'calculators/category.html',
        {
            'category_name': category_name
        }
    )
def health_body(request):
    return render(
        request,
        "calculators/category.html",
        {
            "category_name": "health-body"
        }
    )
def unit_converter(request):
    return render(
        request,
        'calculators/unit-converter/unit-converter.html'
    )
def more_tools(request):
    return render(
        request,
        "calculators/more-tools/more-tools.html"
    )
def basic_calculator(request):
    return render(request, "calculators/basic/basic_calculator.html")

def percentage_calculator(request):
    return render(request, 'calculators/basic/percentage_calculator.html')

def average_calculator(request):
    return render(request, 'calculators/basic/average_calculator.html')
def discount_calculator(request):
    return render(request, 'calculators/basic/discount_calculator.html')
def ratio_calculator(request):
    return render(request, 'calculators/basic/ratio_calculator.html')
def profit_loss_calculator(request):
    return render(request, 'calculators/basic/profit_loss_calculator.html')
def scientific_calculator(request):
    return render(request, "calculators/scientific/calculator.html")
def power_calculator(request):
    return render(request, "calculators/scientific/power.html")
def square_root_calculator(request):
    return render(request, "calculators/scientific/square_root.html")
def quadratic_calculator(request):
    return render(request, "calculators/scientific/quadratic.html")
def geometry_calculator(request):
    return render(
        request,
        "calculators/scientific/geometry.html"
    )

def derivative_calculator(request):
    return render(
        request,
        "calculators/scientific/derivative.html"
    )

def integration_calculator(request):
    return render(
        request,
        "calculators/scientific/integration.html"
    )

def equation_solver(request):
    return render(
        request,
        "calculators/scientific/equation_solver.html"
    )

def banking_finance(request):
    return render(
        request,
        'calculators/banking/banking_finance.html'
    )
def sip_calculator(request):
    return render(request, 'calculators/banking/sip.html')

def fd_calculator(request):
    return render(request, 'calculators/banking/fd.html')

def rd_calculator(request):
    return render(request, 'calculators/banking/rd.html')
def emi_calculator(request):
    return render(
        request,
        'calculators/banking/emi.html'
    )
def simple_interest_calculator(request):
    return render(
        request,
        'calculators/banking/simple_interest.html'
    )
def compound_interest_calculator(request):
    return render(
        request,
        'calculators/banking/compound_interest.html'
    )
def cagr_calculator(request):
    return render(
        request,
        'calculators/banking/cagr.html'
    )
def roi_calculator(request):
    return render(
        request,
        'calculators/banking/roi.html'
    )
def academic(request):
    return render(
        request,
        'calculators/academic/academic.html'
    )
def cgpa_calculator(request):
    return render(
        request,
        'calculators/academic/cgpa.html'
    )
def sgpa_calculator(request):
    return render(
        request,
        'calculators/academic/sgpa.html'
    )
def ygpa_calculator(request):
    return render(
        request,
        'calculators/academic/ygpa.html'
    )
def dgpa_calculator(request):
    return render(
        request,
        'calculators/academic/dgpa.html'
    )
def percentage_converter(request):
    return render(
        request,
        "calculators/academic/percentage.html"
    )
def date_difference(request):
    return render(
        request,
        "calculators/age-date-time/date-difference.html"
    )
def day_calculator(request):
    return render(
        request,
        "calculators/age-date-time/day-calculator.html"
    )
def time_duration(request):
    return render(
        request,
        "calculators/age-date-time/time-duration.html"
    )
def time_addition(request):
    return render(
        request,
        "calculators/age-date-time/time-addition.html"
    )
def date_calculator(request):
    return render(
        request,
        "calculators/age-date-time/date-calculator.html"
    )
def bmi_calculator(request):
    return render(
        request,
        "calculators/health-body/bmi.html"
    )
def health_body(request):
    return render(
        request,
        "calculators/health-body/health-body.html"
    )
def bmr_calculator(request):
    return render(
        request,
        "calculators/health-body/bmr.html"
    )

def ideal_weight_calculator(request):
    return render(
        request,
        'calculators/health-body/ideal-weight.html'
    )
def body_fat_calculator(request):
    return render(
        request,
        'calculators/health-body/bodyfat.html'
    )
def calorie_calculator(request):
    return render(
        request,
        'calculators/health-body/calorie.html'
    )
def random_number(request):
    return render(
        request,
        "calculators/more-tools/random-number.html"
    )
def random_picker(request):
    return render(
        request,
        "calculators/more-tools/random-picker.html"
    )
def word_counter(request):
    return render(
        request,
        "calculators/more-tools/word-counter.html"
    )
def roman_numeral(request):
    return render(
        request,
        "calculators/more-tools/roman-numeral.html"
    )
def text_case_converter(request):
    return render(
        request,
        "calculators/more-tools/text-case-converter.html"
    )
def coin_toss(request):
    return render(
        request,
        "calculators/more-tools/coin-toss.html"
    )