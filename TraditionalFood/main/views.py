from django.shortcuts import render, redirect
from django.http import HttpRequest#, HttpResponsett



RECIPES = [
    # Central Region
    {
        'name': 'الجريش',
        'description': 'طبق أرز سعودي تقليدي مع الدجاج أو اللحم.',
        'ingredients': 'حبوب الجريش، اللبن أو الحليب، البصل، الماء.',
        'instructions': 'تسلق حبوب الجريش مع البصل والماء على نار هادئة ويضاف إليها اللبن أو الحليب، وعند نضجها تقدم وتزين بالسمن أو الزبدة.',
        'image': 'jareesh.jpg',
        'get_it_link': 'https://thechefzco.app.link/0qQUVKEAjLb',
        'map_link': 'https://www.google.com/maps/search/jareesh+restaurant',
        'region': 'المنطقة الوسطى'
    },
    {
        'name': 'المرقوق',
        'description': 'طبق سعودي تقليدي يحتوي على اللحم والبر.',
        'ingredients': 'عجين البر أو قرصان البر، اللحم، البصل، الماء.',
        'instructions': 'تعمل رقائق سميكة من عجين البر، ويغلى اللحم مع الخضروات والبصل ويضاف إليها رقائق عجين البر ويترك ليطبخ مدة ساعة حتى ينضج العجين مع اللحم والخضروات.',
        'image': 'marqooq.png',
        'get_it_link': 'https://example.com/order/marqooq',
        'map_link': 'https://www.google.com/maps/search/marqooq+restaurant',
        'region': 'المنطقة الوسطى'
    },
    {
        'name': 'كبيبة حائل',
        'description': 'طبق شعبي من منطقة حائل.',
        'ingredients': 'لحم مفروم، برغل، بصل، توابل.',
        'instructions': 'تخلط المكونات وتشكل على هيئة كرات وتطهى حتى النضج.',
        'image': 'kubba_hail.png',
        'get_it_link': 'https://example.com/order/kubba_hail',
        'map_link': 'https://www.google.com/maps/search/kubba_hail+restaurant',
        'region': 'المنطقة الوسطى'
    },
    {
        'name': 'الحنيني',
        'description': 'من الحلويات الشتوية حيث أنه يمد الجسم بالطاقة والدفء لاحتوائه على كاربوهيدرات عالية.',
        'ingredients': 'تمر منزوع النوى، دقيق البر، السمن أو الزبدة، اللبن أو الحليب، الزعفران، الماء الساخن.',
        'instructions': 'يتم هرس التمر ويضاف إليه الماء الساخن ودقيق البر، ومن ثم يضاف إليه السمن أو الزبدة مع الهيل المطحون والزعفران.',
        'image': 'hanini.jpg',
        'get_it_link': 'https://example.com/order/hanini',
        'map_link': 'https://www.google.com/maps/search/hanini+restaurant',
        'region': 'المنطقة الوسطى'
    },
    {
        'name': 'الكليجا',
        'description': 'حلوى تقليدية من منطقة القصيم.',
        'ingredients': 'دقيق البر، سكر، دبس التمر، زبدة، بهارات.',
        'instructions': 'تعجن المكونات وتخبز حتى تصبح ذهبية اللون.',
        'image': 'kleija.jpg',
        'get_it_link': 'https://example.com/order/kleija',
        'map_link': 'https://www.google.com/maps/search/kleija+restaurant',
        'region': 'المنطقة الوسطى'
    },
    # Northern Region
    {
        'name': 'المقشوش',
        'description': 'طبق تقليدي من المنطقة الشمالية يتميز ببساطته وقيمته الغذائية العالية.',
        'ingredients': 'دقيق البر، السمن أو الزبدة، العسل.',
        'instructions': 'يعجن دقيق البر بالماء حتى يتكون خليط متماسك، يشكل على هيئة أقراص وتخبز، تقدم مع السمن أو الزبدة والعسل.',
        'image': 'magshoush.png',
        'get_it_link': 'https://example.com/order/magshoush',
        'map_link': 'https://www.google.com/maps/search/magshoush+restaurant',
        'region': 'المنطقة الشمالية'
    },
    {
        'name': 'التطماج',
        'description': 'طبق شعبي من منطقة حائل.',
        'ingredients': 'لحم، برغل، بصل، توابل.',
        'instructions': 'يتم طبخ اللحم مع البرغل والبصل والتوابل حتى ينضج.',
        'image': 'tatmaj.png',
        'get_it_link': 'https://example.com/order/tatmaj',
        'map_link': 'https://www.google.com/maps/search/tatmaj+restaurant',
        'region': 'المنطقة الشمالية'
    },
    # Western Region
    {
        'name': 'المعدوس',
        'description': 'طبق تقليدي من الأرز والعدس.',
        'ingredients': 'أرز، عدس، بصل، بهارات.',
        'instructions': 'يطهى الأرز مع العدس والبصل والبهارات حتى ينضج.',
        'image': 'madous.png',
        'get_it_link': 'https://example.com/order/madous',
        'map_link': 'https://www.google.com/maps/search/madous+restaurant',
        'region': 'المنطقة الغربية'
    },
    {
        'name': 'السوبيا',
        'description': 'مشروب تقليدي شعبي في المنطقة الغربية.',
        'ingredients': 'خبز جاف، سكر، ماء، بهارات.',
        'instructions': 'ينقع الخبز في الماء مع السكر والبهارات حتى يتخمر ويصفى.',
        'image': 'sobia.png',
        'get_it_link': 'https://example.com/order/sobia',
        'map_link': 'https://www.google.com/maps/search/sobia+restaurant',
        'region': 'المنطقة الغربية'
    },
    # Southern Region
    {
        'name': 'العصيدة',
        'description': 'طبق شعبي من المنطقة الجنوبية.',
        'ingredients': 'دقيق البر، لبن، زبدة.',
        'instructions': 'يخلط الدقيق بالماء حتى يتماسك، يطهى ويقدم مع اللبن والزبدة.',
        'image': 'aseeda.png',
        'get_it_link': 'https://example.com/order/aseeda',
        'map_link': 'https://www.google.com/maps/search/aseeda+restaurant',
        'region': 'المنطقة الجنوبية'
    },
    {
        'name': 'المقروطة',
        'description': 'طبق تقليدي من المنطقة الجنوبية يحتوي على التمر.',
        'ingredients': 'تمر، دقيق، سمن.',
        'instructions': 'تخلط المكونات وتشكل على هيئة أصابع وتخبز.',
        'image': 'maqrootha.png',
        'get_it_link': 'https://example.com/order/maqrootha',
        'map_link': 'https://www.google.com/maps/search/maqrootha+restaurant',
        'region': 'المنطقة الجنوبية'
    },
    # Eastern Region
    {
        'name': 'الهريس',
        'description': 'طبق تقليدي من المنطقة الشرقية يتميز بقوامه الكريمي.',
        'ingredients': 'قمح، لحم، ماء، ملح.',
        'instructions': 'يُطهى القمح واللحم في الماء حتى يتماسك القوام، ويصبح ناعمًا وكريميًا.',
        'image': 'harees.png',
        'get_it_link': 'https://example.com/order/harees',
        'map_link': 'https://www.google.com/maps/search/harees+restaurant',
        'region': 'المنطقة الشرقية'
    },
    {
        'name': 'خبز الحمر',
        'description': 'خبز تقليدي من المنطقة الشرقية يتميز بلونه الداكن.',
        'ingredients': 'دقيق البر، ماء، خميرة، ملح.',
        'instructions': 'يعجن الدقيق بالماء والخميرة والملح، ويترك ليختمر ثم يخبز حتى ينضج.',
        'image': 'khubz_al_hamr.png',
        'get_it_link': 'https://example.com/order/khubz_al_hamr',
        'map_link': 'https://www.google.com/maps/search/khubz_al_hamr+restaurant',
        'region': 'المنطقة الشرقية'
    }
]



def home(request: HttpRequest):
    regions = {
    'المنطقة الوسطى': 'Central Region',
    'المنطقة الشمالية': 'Northern Region',
    'المنطقة الغربية': 'Western Region',
    'المنطقة الجنوبية': 'Southern Region',
    'المنطقة الشرقية': 'Eastern Region'
    }
        
    return render(request, 'main/home.html', {'recipes': RECIPES, 'regions': regions})


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
        {'name': 'المنطقة الوسطى', 'description': 'الرياض، القصيم، حائل', 'image': 'central-region.png'},
        {'name': 'المنطقة الشمالية', 'description': 'تبوك، الجوف، الحدود الشمالية', 'image': 'northern-region.png'},
        {'name': 'المنطقة الغربية', 'description': 'مكة المكرمة، المدينة المنورة، جدة', 'image': 'western-region.png'},
        {'name': 'المنطقة الجنوبية', 'description': 'عسير، جازان، نجران', 'image': 'southern-region.png'},
        {'name': 'المنطقة الشرقية', 'description': 'الدمام، الأحساء، الظهران', 'image': 'eastern-region.png'}
    ]
    return render(request, 'main/regions.html', {'regions': regions, 'recipes': RECIPES})


restaurants = [
    {
        'name': 'عسيب',
        'image': 'aseeb.jpeg',
        'location': 'طريق أنس بن مالك, Alyasmin, Riyadh 13325',
        'website_link': 'http://aseeb.com.sa/',
        'map_link': 'https://maps.app.goo.gl/zWhFhTQwd6U5St1w9'
    },
    {
        'name': 'ثرى',
        'image': 'restaurant2.jpg',
        'location': 'سكّة سكوير, Abi Bakr As Siddiq Branch Rd, An Narjis, Riyadh 13327',
        'website_link': 'https://www.instagram.com/thara_saudi?igsh=Z3IzY3M2a2E5dnNv',
        'map_link': 'https://maps.app.goo.gl/BqfQorW6rxCW5mmt5'
    },
]

def restaurants_view(request):
    return render(request, 'main/restaurants.html', {'restaurants': restaurants})