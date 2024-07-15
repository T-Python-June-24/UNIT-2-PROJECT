from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from urllib.parse import quote, unquote


def get_dark_mode(request):
    return request.COOKIES.get('dark_mode', 'false') == 'true'

def index(request):
    dark_mode = get_dark_mode(request)
    response = render(request, 'saudi_arabia/index.html', {'dark_mode': dark_mode})
    response.set_cookie('dark_mode', str(dark_mode).lower(), max_age=31536000)  
    return response

def dark_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', 'saudi_arabia:index'))
    response.set_cookie('dark_mode', 'true', max_age=31536000)  
    return response

def light_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', 'saudi_arabia:index'))
    response.set_cookie('dark_mode', 'false', max_age=31536000)  
    return response

def history(request):
    history = {
        'islamic_heritage': {
            'title': 'Islamic Heritage',
            'content': 'Saudi Arabia, as the birthplace of Islam, has a deep commitment to preserving and promoting Islamic values and serving Muslims worldwide.',
            'image': 'images/Makkah.jpg',
            'modal_title': 'Saudi Arabia: Guardian of Islamic Heritage',
            'modal_content': 'As the heartland of Islam, Saudi Arabia plays a crucial role in preserving and promoting Islamic heritage. The Kingdom is home to the Two Holy Mosques in Makkah and Madinah, towards which Muslims worldwide turn in prayer. Saudi Arabia has implemented numerous initiatives to serve Islam and Muslims globally. The Pilgrim Experience Program, launched in 2019, aims to enrich the spiritual journeys of millions of Hajj and Umrah pilgrims by providing world-class facilities, improved infrastructure, and digitized services[2]. Additionally, the Ministry of Islamic Affairs, Dawah and Guidance oversees important Islamic activities, including supervising mosques, printing the Quran, organizing Quranic competitions, and supporting Islamic communities worldwide[3]. These efforts demonstrate Saudi Arabia\'s ongoing commitment to its Islamic responsibilities and its role as a leader in the Muslim world[1].'
        },
        'first_saudi_state': {
            'title': 'First Saudi State',
            'content': 'The First Saudi State was established in 1744 when Muhammad ibn Saud formed an alliance with religious leader Muhammad ibn Abd al-Wahhab.',
            'image': 'images/first-state.jpg',
            'modal_title': 'The First Saudi State and Wahhabi Alliance',
            'modal_content': 'The First Saudi State emerged in 1744 when Muhammad ibn Saud, emir of Diriyah, formed an alliance with religious reformer Muhammad ibn Abd al-Wahhab. This alliance combined political power with religious ideology, laying the foundation for Saudi rule. The state expanded its control over much of the Arabian Peninsula, including the Hejaz region. However, it faced opposition from the Ottoman Empire, which saw it as a threat to its authority. In 1818, Ottoman forces destroyed Diriyah, effectively ending the First Saudi State, but its legacy would continue to shape the region\'s future.'
        },
        'unification': {
            'title': 'Unification of Saudi Arabia',
            'content': 'In the early 20th century, Abdulaziz ibn Saud began a campaign to unify the Arabian Peninsula, culminating in the founding of Saudi Arabia in 1932.',
            'image': 'images/unification.jpg',
            'modal_title': 'The Birth of Modern Saudi Arabia',
            'modal_content': 'The modern Kingdom of Saudi Arabia was born out of a 30-year campaign of unification led by Abdulaziz ibn Saud. Beginning with the capture of Riyadh in 1902, Abdulaziz gradually conquered or allied with various tribes and regions. He defeated the Rashidi dynasty, conquered the Hejaz, and united the diverse regions of the peninsula. On September 23, 1932, Abdulaziz proclaimed the establishment of the Kingdom of Saudi Arabia, with himself as its first king. This date is now celebrated as Saudi National Day.'
        },
        'modern_saudi': {
            'title': 'Modern Saudi Arabia',
            'content': 'Since its founding, Saudi Arabia has transformed from a desert kingdom into a major global player, driven by oil wealth and modernization efforts.',
            'image': 'images/modern_saudi.jpg',
            'modal_title': 'Saudi Arabia in the Modern Era',
            'modal_content': 'The discovery of oil in 1938 transformed Saudi Arabia\'s economy and global significance. Under successive kings, the country has undergone rapid modernization while maintaining its Islamic heritage. Key developments include the oil boom of the 1970s, the Gulf War of 1990-91, and recent reform initiatives like Vision 2030. Saudi Arabia plays a crucial role in global oil markets, Middle Eastern politics, and Islamic affairs as the custodian of the Two Holy Mosques. The country continues to balance tradition with modernization, facing challenges and opportunities in the 21st century.'
        }
    }
    dark_mode = get_dark_mode(request)
    response = render(request, 'saudi_arabia/history.html', {'dark_mode': dark_mode, 'history': history})
    response.set_cookie('dark_mode', str(dark_mode).lower(), max_age=31536000)
    return response

def cuisine(request):
    cuisines = [
        {
            'name': 'Traditional Saudi Cuisine - Kabsa',
            'image': 'images/Kabsa.jpg',
            'ingredients': ['Lamb', 'Chicken', 'Rice', 'Dates', 'Cardamom', 'Cinnamon', 'Cloves', 'Black lime', 'Nutmeg', 'Yogurt', 'Onions', 'Garlic'],
            'description': 'Traditional Saudi cuisine is deeply rooted in Bedouin culture and Islamic traditions. Kabsa, the national dish, exemplifies this cuisine with its fragrant rice and meat combination, seasoned with aromatic spices.',
        },
        {
            'name': 'Najdi Cuisine - Jareesh',
            'image': 'images/Jareesh.jpg',
            'ingredients': ['Wheat', 'Lamb', 'Yogurt', 'Onions', 'Tomatoes', 'Garlic', 'Cumin', 'Coriander', 'Cardamom', 'Dried limes'],
            'description': 'Najdi cuisine, from the central region of Saudi Arabia, is known for hearty dishes like Jareesh. This cracked wheat dish, often served with meat and garnished with fried onions, reflects the region\'s agricultural heritage and adaptation to the desert climate[1].',
        },
        {
            'name': 'Hijazi Cuisine - Saleeg',
            'image': 'images/Saleeg.jpg',
            'ingredients': ['Rice', 'Chicken', 'Milk', 'Cardamom', 'Cinnamon', 'Black pepper', 'Ghee', 'Onions', 'Garlic'],
            'description': 'Hijazi cuisine, from the western region of Saudi Arabia, shows influences from pilgrims and traders who have visited Mecca and Medina over centuries. Saleeg, a creamy rice dish cooked with milk and meat, is a popular comfort food in this region.',
        },
        {
            'name': 'Tharid',
            'image': 'images/Tharid.jpg',
            'ingredients': ['Bread', 'Meat broth', 'Lamb or chicken', 'Vegetables', 'Spices'],
            'description': 'Tharid is a traditional dish said to be a favorite of Prophet Muhammad. It consists of pieces of bread soaked in a flavorful meat broth, topped with meat and vegetables. This comforting dish is often served during Ramadan and cold weather[2].',
        },
        {
            'name': 'Mutabbaq',
            'image': 'images/Mutabbaq.jpg',
            'ingredients': ['Flour', 'Eggs', 'Minced meat', 'Onions', 'Spices'],
            'description': 'Mutabbaq, also known as murtabak, is a stuffed pancake or pan-fried bread filled with minced meat, eggs, and vegetables. It\'s a popular street food in Saudi Arabia, often served as a snack or light meal[3].',
        },
        {
            'name': 'Qursan',
            'image': 'images/Qursan.jpg',
            'ingredients': ['Thin bread', 'Meat broth', 'Lamb or chicken', 'Vegetables', 'Spices'],
            'description': 'Qursan is a traditional Bedouin dish made with thin, crispy bread discs that are broken into pieces and soaked in a savory broth made with meat and vegetables. It\'s a comforting and filling meal, often enjoyed during colder months[4].',
        },
        {
            'name': 'Harees',
            'image': 'images/Harees.jpg',
            'ingredients': ['Wheat berries', 'Chicken or lamb', 'Cinnamon', 'Cumin', 'Cardamom', 'Ghee'],
            'description': 'Harees is a dish made from wheat berries and meat (usually chicken or lamb) cooked together until they form a thick, porridge-like consistency. It\'s often seasoned with cinnamon, cumin, and cardamom, and topped with ghee before serving. Harees is particularly popular during Ramadan and other festive occasions[5].',
        },
    ]
    
    for cuisine in cuisines:
        encoded_cuisine_name = quote(cuisine['name'])
        cookie_name = f'selected_ingredients_{encoded_cuisine_name}'
        selected_ingredients = request.COOKIES.get(cookie_name, '[]')
        try:
            cuisine['selected_ingredients'] = json.loads(unquote(selected_ingredients))
        except json.JSONDecodeError:
            cuisine['selected_ingredients'] = []
    
    dark_mode = get_dark_mode(request)
    response = render(request, 'saudi_arabia/cuisine.html', {'dark_mode': dark_mode, 'cuisines': cuisines})
    response.set_cookie('dark_mode', str(dark_mode).lower(), max_age=31536000) 
    return response

def save_selected_ingredients(request):
    try:
        data = json.loads(request.body)
        cuisine_name = data.get('cuisine_name')
        selected_ingredients = data.get('selected_ingredients')
        
        if not cuisine_name or selected_ingredients is None:
            return JsonResponse({'status': 'error', 'message': 'Missing cuisine_name or selected_ingredients'}, status=400)
        
        encoded_cuisine_name = quote(cuisine_name)
        
        response = JsonResponse({'status': 'success'})
        response.set_cookie(f'selected_ingredients_{encoded_cuisine_name}', 
                            json.dumps(selected_ingredients), 
                            max_age=31536000)  # 1 year
        return response
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    
def kings(request):
    kings = [
        {
            'name': 'King Abdulaziz',
            'image': 'images/king-abdulaziz.jpg',
            'description': 'Founder of Saudi Arabia and its first king, ruling from 1932 to 1953. He unified the kingdom and laid the foundation for modern Saudi Arabia.',
        },
        {
            'name': 'King Saud',
            'image': 'images/king-saud.jpg',
            'description': "Second king of Saudi Arabia, ruling from 1953 to 1964. He focused on developing the country's infrastructure and education system.",
        },
        {
            'name': 'King Faisal',
            'image': 'images/king-faisal.jpg',
            'description': 'Third king of Saudi Arabia, ruling from 1964 to 1975. He was known for his modernization efforts and played a significant role in the 1973 oil crisis.',
        },
        {
            'name': 'King Khalid',
            'image': 'images/king-khalid.jpg',
            'description': 'Fourth king of Saudi Arabia, ruling from 1975 to 1982. He continued the modernization policies of his predecessor and oversaw a period of economic growth.',
        },
        {
            'name': 'King Fahad',
            'image': 'images/king-fahad.jpg',
            'description': 'Fifth king of Saudi Arabia, ruling from 1982 to 2005. He implemented significant economic and social reforms and played a crucial role during the Gulf War.',
        },
        {
            'name': 'King Abdullah',
            'image': 'images/king-abdullah.jpg',
            'description': 'Sixth king of Saudi Arabia, ruling from 2005 to 2015. He was known for his efforts to promote dialogue between different faiths and cultures, and for initiating various reform programs.',
        },
        {
            'name': 'King Salman',
            'image': 'images/king-salman.jpg',
            'description': 'Seventh and current king of Saudi Arabia, ruling since 2015. He has implemented significant social and economic reforms, including granting women the right to drive and diversifying the economy.',
        }
    ]
    dark_mode = get_dark_mode(request)
    response = render(request, 'saudi_arabia/kings.html', {'dark_mode': dark_mode, 'kings': kings})
    response.set_cookie('dark_mode', str(dark_mode).lower(), max_age=31536000)
    return response 


def future(request):
    dark_mode = get_dark_mode(request)
    response = render(request, 'saudi_arabia/future.html', {'dark_mode': dark_mode})
    response.set_cookie('dark_mode', str(dark_mode).lower(), max_age=31536000)
    return response