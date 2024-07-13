from django.shortcuts import render, redirect

def get_dark_mode(request):
    return request.COOKIES.get('dark_mode', 'false') == 'true'

def index(request):
    dark_mode = get_dark_mode(request)
    return render(request, 'saudi_arabia/index.html', {'dark_mode': dark_mode})

def dark_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', 'saudi_arabia:index'))
    response.set_cookie('dark_mode', 'true', max_age=31536000)  # 1 year
    return response

def light_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', 'saudi_arabia:index'))
    response.set_cookie('dark_mode', 'false', max_age=31536000)  # 1 year
    return response

def history(request):
    history={
        'ancient': {
            'title': 'Ancient Arabia',
            'content': 'Ancient Arabia was home to many civilizations, including the Nabataeans, known for their rock-cut architecture in Petra. The region was also a hub for trade routes connecting Asia, Africa, and Europe.',
            'image': 'images/history1.jpg',
            'modal_title': 'Ancient Arabia',
            'modal_content': 'Ancient Arabia was home to many civilizations, including the Nabataeans, known for their rock-cut architecture in Petra. The region was also a hub for trade routes connecting Asia, Africa, and Europe.',
        },
        'golden': {
            'title': 'Islamic Golden Age',
            'content': 'During the Islamic Golden Age, Arabia was a center of learning and innovation. Scholars made significant contributions to mathematics, astronomy, medicine, and philosophy, influencing the Renaissance in Europe.',
            'image': 'images/Makkah.jpg',
            'modal_title': 'Islamic Golden Age',
            'modal_content': 'During the Islamic Golden Age, Arabia was a center of learning and innovation. Scholars made significant contributions to mathematics, astronomy, medicine, and philosophy, influencing the Renaissance in Europe.',
        },
        'modern': {
            'title': 'Modern Saudi Arabia',
            'content': 'The Kingdom of Saudi Arabia was founded in 1932 by King Abdulaziz Al Saud. Since then, it has undergone rapid modernization and development, becoming a major global oil producer and a key player in international affairs.',
            'image': 'images/modern_saudi.jpg',
            'modal_title': 'Modern Saudi Arabia',
            'modal_content': 'The Kingdom of Saudi Arabia was founded in 1932 by King Abdulaziz Al Saud. Since then, it has undergone rapid modernization and development, becoming a major global oil producer and a key player in international affairs. The country has also been implementing significant social and economic reforms in recent years.',
        },
    }
    dark_mode = get_dark_mode(request)
    return render(request, 'saudi_arabia/history.html', {'dark_mode': dark_mode, 'history': history})