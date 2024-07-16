from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse 

# Create your views here.

def home_view(request:HttpRequest)->render:
    return render(request,"main/index.html")

def change_theme(request: HttpRequest) -> HttpResponse:
    response = redirect(request.GET.get("next", "/"))
    # the default is light mode.
    if "dark_theme" not in request.COOKIES:
        response.set_cookie("dark_theme", "true")
    else:  
        current_value = request.COOKIES.get("dark_theme")
        if current_value == "true":
            
            response.set_cookie("dark_theme", "false")
        else:
            
            response.set_cookie("dark_theme", "true")
    
    return response

def njdiArdah_view(request:HttpRequest)->render:
    poets=[{
        "name":"Naser Alorainee",
        "img":"images/naserAlareeni.jpg",
        "city":"al diriyah"

    },
    {
        "name":"Abdullah Alsobai",
        "img":None,
        "city":"Shaqra"
    },
    {
        "name":"Mohammed Aloani",
        "img":"images/mohammedAloanii.jpg",
        "city":"alrabieia"
    },
    {
        "name":"Fhaed bin Dhaemm",
        "img":None,
        "city":"Riyadh"
    },
    {
        "name":"Abdurhman Alboardi",
        "img":None,
        "city":"Shaqra"
    }
    ]
    return render(request,"main/njdiArdah.html",context={"poets":poets})

def southArdah_view(request:HttpRequest)->render:
    infos=[
        
        {
        "header":"The Southern Ardha",
        "body":''' This is a Saudi traditional folkloric performance, composed of a poet and players (Arradha) and a drummer. It is characterized by its organization and beauty, and is performed during celebrations and weddings. The Ardha is formed of two sections of players, front and back, with a passage between them. Each section consists of two, two people. The poet stands in front of the first group and recites the opening lines of the poem, saying "Shallo", meaning "Play with it". The drummer then starts and quickly moves to the second group, reciting the ending lines of the verse. Back then, there was no microphone, so the two groups would alternate reciting the opening and ending lines vocally, until the poem is completed. Then another poet comes and says "Khallooha" (Leave it) and recites another poem, either to the same tune or a different one. The drummers' task is to light a fire in the middle of the performance area to warm up the Zir, which is a large tambourine (teb'a) that plays continuously, and a smaller tambourine (muwahid) that plays on the third bar, and skips the next one. This is the original Ardha performance.''',    
        }
        ,
        {
            "header":"History",
            "body":'''According to Qinan Al-Zahrani, a researcher in folk heritage, the current form of the Southern Ardha dates back to before the 10th century AH (Hijri calendar). He adds that the Ardha, as a folk heritage, cannot have its beginnings determined, as it has evolved in the southern environment over hundreds of years prior to the 10th century. However, the oldest poetic text known in the Ardha and passed down to the present day dates back to the 10th century AH. At that time, the poetry of the Ardha was not limited to the Shaqr Al-Radd poetry, but rather belonged to the category of Jinas (rhymed prose).'''

        },
        {
            "header":"Rhythms and Melodies",
            "body":'''The Ardha has two rhythms: a binary (flowing unit) suitable for the Raddadin, and a slow (Raa'ih) rhythm in the triple meter and its multiples (Tam Tak Tak).

As for the meters of Ardha poetry, the poet Abdulwahid Al-Zahrani says that folk poetry is the legitimate offspring of classical poetry, and therefore its meters and rhythms are very close to the meters of prosodic poetry. When we scan the poetic verse in Ardha poetry, we find that it perfectly matches the meters of Al-Khalil bin Ahmad Al-Farahidi, with a slight difference. In the poetry of the South, the Milalah measure is used, i.e., Yalal Yalal, instead of the feet upon which classical poetry is built.

The source of strength in southern poetry is the same as its weakness, as it has adhered to only one of the rhetorical embellishments, which is Jinas (paronymous rhyme). Southern poetry has confined itself to this one type of rhetorical embellishment, while we know that there are various types of such embellishments. The Shaqr (paronymous rhyme) is a source of strength in terms of the challenge, but it has weakened southern poetry by limiting it and confining southern poets within this southern region of Saudi Arabia.

The poetry of the Southern Ardha has a uniqueness that may be lacking in other genres of poetry, and this uniqueness is manifested in the art of Shaqr (paronymous rhyme).'''
        },
        {
            "header":"Performance of Al-Ardah: A Collaborative Art of Poetry, Rhythm, and Movement",
            "body":'''Al-Ardah is an improvisational art form that demands a high level of skill from the poet, who must be well-versed in the art of "shaqr" (a type of poetic wordplay) in order to participate. Shaqr is an essential element for those who wish to enter the world of Al-Ardah, and it also requires the Al-Ardah troupe to maintain harmony and coordination to the rhythm of the tambourine in synchronized formations. The term "Ardah" is derived from the Arabic word "ard" meaning "to show" or "to parade." This reflects its origins as a peaceful military display that emphasized the unity, morale, and strength of a tribe.

Al-Ardah is performed with one or more poets accompanied by the tambourine, surrounded by rows of performers whose number is not fixed. The performers carry swords, rifles, or daggers and march in a measured step in a two-person formation (two people side by side) in a circular motion. They then return to a single circular line facing the center of the field to follow the poets and imitate their movements in a display of spectacle. The performance pauses for a phase of improvisation and response among the poets, and then resumes its circular motion.

Al-Ardah varies from region to region, and even within the same region, there are variations in style and execution.

Shaqr: The Poetic Soul of Al-Ardah

Shaqr in the art of Al-Ardah is a colloquial term equivalent to "jinas" in Arabic, which refers to the similarity of two words in pronunciation but difference in meaning. No one can deny the pleasant sound and beautiful rhythm of shaqr, which delights the ears and gladdens the hearts. With the presence of shaqr, Al-Ardah becomes an art form that engages everyone: the poet, the performers, the audience, and the tambourine player. Shaqr has become a distinctive feature of Southern Al-Ardah, so much so that some have come to refer to the poetry of Southern Al-Ardah as "shaqr" due to its unique use of this poetic device.

What is called a "shatr" (a line of poetry) in Arabic poetry is called a "bayt" (a complete poem) in Southern Al-Ardah poetry. The poet who improvises must prepare the ground for the other poet, a process known as "farash." The response must follow the path of shaqr, and it is necessary to find a different meaning for the words at the end of the first poet's verses than what the first poet intended, whether in full or in part. This depends on the poet's acquired and inherited abilities, their talent, and their cultural, scientific, and intellectual potential. This requires a strong memory for the poet's poem and quick thinking to enable them to understand the poet's intentions, interpret their meanings, and respond accordingly. Their response must reach the opponent in an indirect manner without being direct, drawing upon the responder's knowledge and cultural background, as well as their charisma and acceptance by the audience, and employing proverbs and sayings. In doing so, they weave unique words in a creative way that demonstrates their talent and distinguishes one poet from another. Thus, the audience begins to classify poets based on their response skills and their originality, as well as their melody.

I hope this translation is helpful. Please let me know if you have any other questions.'''
        },
        {
            "header":"Al-Khatwah and Al-Samer",
            "body":'''Al-Khatwah is a traditional Saudi dance performed by two lines of dancers facing each other, without music or drums. The dancers take steps forward and backward (takseer) in a rhythmic pattern, chanting phrases like Ala yakhut mooz (Don't step on the banana), Khoot barak (Blessing step), and "Khoot rayhan" (Basil step).'''
        }
        
        
        ]
    
    poets=[{
        "name":"Muhammad bin Ma'id",
        "img":"images/aboJaeedi.jpg",
        "city":"al Baha"

    },
    {
        "name":"Mubarak Abu Olag",
        "img":"images/aboolag.jpeg",
        "city":"Al aqiq"
    },
    {
        "name":"Aaydah bin Tuwair",
        "img":"images/aidahalmalki.jpg",
        "city":"Bakhir"
    },
    {
       "name":"Abdulwaheed Al Zahrani",
        "img":"images/abdaluahid.jpg",
        "city":"Al baha"
    },
    {
        "name":"Humīl bin Sharaf",
        "img":"images/hmialbinsharf.jpeg",
        "city":"Al baha"
    },
    {
        "name":"mohammed bin thaib",
        "img":"images/mohammedbinthaib.jpg",
        "city":"Bisah"

    }

    ]
    return render(request,"main/southArdah.html",context={"info":infos,"poets":poets})