from django.shortcuts import render, redirect
from django.http import HttpRequest#, HttpResponsett



RECIPES = [
    {
        'name': 'كبسة',
        'description': 'طبق أرز سعودي تقليدي مع الدجاج أو اللحم.',
        'ingredients': 'أرز، دجاج، توابل',
        'instructions': 'اطبخ الأرز مع التوابل والدجاج.',
        'image': 'kabsa.jpg',
        'get_it_link': 'https://example.com/order/kabsa',
        'map_link': 'https://www.google.com/maps/search/kabsa+restaurant',
        'region': 'المنطقة الوسطى'
    },
    {
        'name': 'مندي',
        'description': 'طبق تقليدي من اليمن يحظى بشعبية كبيرة في السعودية.',
        'ingredients': 'أرز، لحم، توابل',
        'instructions': 'اطبخ الأرز مع التوابل واللحم.',
        'image': 'mandi.jpg',
        'get_it_link': 'https://example.com/order/mandi',
        'map_link': 'https://www.google.com/maps/search/mandi+restaurant',
        'region': 'المنطقة الجنوبية'
    }
]



def home(request: HttpRequest):
    return render(request, 'main/home.html')


def recipe_list(request: HttpRequest):
    return render(request, 'main/recipe_list.html', {'recipes': RECIPES})



def recipe_detail(request: HttpRequest, recipe_name):
    recipe = next((r for r in RECIPES if r['name'] == recipe_name), None)
    if recipe:
        return render(request, 'main/recipe_detail.html', {'recipe': recipe})
    else:
        return render(request, 'main/404.html', {'message': 'لم يتم العثور على الوصفة'})


def regions(request: HttpRequest):
    regions = [
        {'name': 'المنطقة الوسطى', 'description': 'الرياض، القصيم، حائل'},
        {'name': 'المنطقة الشمالية', 'description': 'تبوك، الجوف، الحدود الشمالية'},
        {'name': 'المنطقة الغربية', 'description': 'مكة المكرمة، المدينة المنورة، جدة'},
        {'name': 'المنطقة الجنوبية', 'description': 'عسير، جازان، نجران'},
        {'name': 'المنطقة الشرقية', 'description': 'الدمام، الأحساء، الظهران'}
    ]
    return render(request, 'main/regions.html', {'regions': regions, 'recipes': RECIPES})