from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(
            'category/banking-finance/',
            views.banking_finance,
            name='banking_finance'
        ),
    path(
        'category/academic/',
        views.academic,
        name='academic'
    ),
    path(
        "category/age-date-time/",
        views.age_date_time,
        name="age_date_time"
    ),
    path(
        "category/health-body/",
        views.health_body,
        name="health_body"
    ),
    path(
        "unit-converter/",
        views.unit_converter,
        name="unit_converter"
    ),
    path(
        "more-tools/",
        views.more_tools,
        name="more_tools"
    ),
    path('category/<str:category_name>/', views.category, name='category'),
    path('basic/calculator/', views.basic_calculator, name='basic_calculator'),
    path('percentage/calculator/', views.percentage_calculator, name='percentage_calculator'),
    path('average/calculator/', views.average_calculator, name='average_calculator'),
    path('discount/calculator/', views.discount_calculator, name='discount_calculator'),
    path('ratio/calculator/', views.ratio_calculator, name='ratio_calculator'),
    path('profit-loss/calculator/', views.profit_loss_calculator, name='profit_loss_calculator'),

    path("scientific/calculator/", views.scientific_calculator, name="scientific_calculator"),
    path("scientific/power/", views.power_calculator, name="power_calculator"),
    path("scientific/square-root/", views.square_root_calculator, name="square_root_calculator"),
    path("scientific/quadratic/", views.quadratic_calculator, name="quadratic_calculator"),
    path("scientific/geometry/", views.geometry_calculator, name="geometry_calculator"),
    path("scientific/derivative/",views.derivative_calculator,name="derivative_calculator"),
    path("scientific/integration/",views.integration_calculator,name="integration_calculator"),
    path("scientific/equation-solver/", views.equation_solver, name="equation_solver"),

    path('sip-calculator/', views.sip_calculator, name='sip_calculator'),
    path('fd-calculator/', views.fd_calculator, name='fd_calculator'),
    path('rd-calculator/', views.rd_calculator, name='rd_calculator'),
    path(
        'emi-calculator/',
        views.emi_calculator,
        name='emi_calculator'
    ),
    path(
        'simple-interest-calculator/',
        views.simple_interest_calculator,
        name='simple_interest_calculator'
    ),
    path(
        'compound-interest-calculator/',
        views.compound_interest_calculator,
        name='compound_interest_calculator'
    ),
    path(
        'cagr-calculator/',
        views.cagr_calculator,
        name='cagr_calculator'
    ),
    path(
        'roi-calculator/',
        views.roi_calculator,
        name='roi_calculator'
    ),
    path(
        'cgpa-calculator/',
        views.cgpa_calculator,
        name='cgpa_calculator'
    ),
    path(
        'sgpa-calculator/',
        views.sgpa_calculator,
        name='sgpa_calculator'
    ),
    path(
        'ygpa-calculator/',
        views.ygpa_calculator,
        name='ygpa_calculator'
    ),
    path(
        'dgpa-calculator/',
        views.dgpa_calculator,
        name='dgpa_calculator'
        ),
    path(
        "percentage-converter/",
        views.percentage_converter,
        name="percentage_converter"
    ),
    path(
        "age-calculator/",
        views.age_calculator,
        name="age_calculator"
    ),
    path(
        "date-difference/",
        views.date_difference,
        name="date_difference"
    ),
    path(
        "day-calculator/",
        views.day_calculator,
        name="day_calculator"
    ),
    path(
        "time-duration/",
        views.time_duration,
        name="time_duration"
    ),
    path(
        "time-addition/",
        views.time_addition,
        name="time_addition"
    ),
    path(
        "date-calculator/",
        views.date_calculator,
        name="date_calculator"
    ),
    path(
        "bmi-calculator/",
        views.bmi_calculator,
        name="bmi_calculator"
    ),
    path(
        "bmr-calculator/",
        views.bmr_calculator,
        name="bmr_calculator"
    ),
    path(
        "ideal-weight-calculator/",
        views.ideal_weight_calculator,
        name="ideal_weight_calculator"
    ),
    path(
        "body-fat-calculator/",
         views.body_fat_calculator,
         name="body_fat_calculator"
         ),
    path(
        "calorie-calculator/",
        views.calorie_calculator,
        name="calorie_calculator"
    ),
    path(
        "more-tools/random-number/",
        views.random_number,
        name="random_number"
    ),
    path(
        "more-tools/random-picker/",
        views.random_picker,
        name="random_picker"
    ),
    path(
        "more-tools/word-counter/",
        views.word_counter,
        name="word_counter"
    ),
    path(
        "more-tools/roman-numeral/",
        views.roman_numeral,
        name="roman_numeral"
    ),
    path(
        "more-tools/text-case-converter/",
        views.text_case_converter,
        name="text_case_converter"
    ),
    path(
        "more-tools/coin-toss/",
        views.coin_toss,
        name="coin_toss"
    ),

]