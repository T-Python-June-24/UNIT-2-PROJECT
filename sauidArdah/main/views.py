from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse ,FileResponse
import json

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


def dahaArdah(request:HttpRequest)->render:

    infos=[
                
                {
                "header":"Al-dahha",
                "body":'''Al-dahha, as it is called by the people of the Arabian Peninsula, is a Bedouin dance practiced in Jordan, the Negev region of Palestine, northern Saudi Arabia, some Gulf states, the valleys of Syria and Iraq, Hauran, and the Sinai Peninsula. Al-dahha was practiced in ancient times before wars to stir up enthusiasm among the members of the tribe, and at the end of ancient battles, it was used to describe the battle and the heroism and actions that took place in it. Now it is practiced on wedding occasions, holidays, and other celebrations, and it combines the art of poetry, dance, and chants.'''
                }
                ,
                {
                    "header":"Origin",
                    "body":'''The origin of this dance is traced back to a popular story: "A caravan of pilgrims was passing through the desert when they noticed thieves watching them while they slept at night. Fearing for their lives, they agreed to clap their hands and make sounds like the rumbling of camels to make the thieves believe they were a large group and scare them off. This strategy was successful in driving away the thieves, and the dance, known as al-dahha, spread as a folk dance. However, the notion that it is linked to the Battle of Dhi Qar is a misconception. The details of the Battle of Dhi Qar are well-documented in history books, and there is no mention of al-dahha.

        '''
                                },
                                {
                    "header":"Performance",
                    "body":'''Al-dahha is performed as a group dance. The men line up in one or two facing rows, and the poet, who stands in the middle of one row, sings his chanted poem, which resembles the hajini style. The rows respond in turn (al-raddadah). The agreed-upon line is gradually passed between each verse recited by the poet. The poems vary from praise and pride to remembrance and praise of God, joy, and love. It is performed in a narrative style, which is the essence of what has been agreed upon as a narrative storytelling position for a battle or a description of a homeland or satire or praise. Sometimes, the hashsh or mahoushi stands in front of the row or between the rows and performs the mahoushi dance between the rows.

        The movement of the dahha comes at the end of the poem, and clapping is used as a rhythmic sound. Al-dahha is distinguished by its enthusiasm in its kinetic performance and requires the participant to reconcile his kinetic and respiratory performance so that he can keep pace with the rest of the participants. The poet of al-dahha is called the bad'a, and the poem of al-dahha is known to others as the bid'ah.'''
                                },
                    {
                        "header":"Intangible Heritage List",
                        "body":"In 2018, UNESCO inscribed al-dahha, as it is called in Jordan, on the Representative List of the Intangible Cultural Heritage of Humanity, during the annual meeting of the Committee for the Safeguarding of Intangible Cultural Heritage held in Port Louis, Mauritius."
                    }
                ]
    poets=[{
        "name":"salem aljbhl",
        "img":"images/salemdaha.jpg",
        "city":"Abha"

    },
    {
        "name":"Abdullah mushni",
        "img":"images/abdullahmashny.jpeg",
        "city":"njd"
    },
    ]
    
    



    return render(request,"main/daha.html",context={"info":infos,"poets":poets})


def qazwaiArdah_view(request:HttpRequest)->render:
    infos=[
        
        {
        "header":"The Qazwai Ardha",
        "body":'''A Martial Folk Art of Saudi Arabia
Qazou'i is a martial folk dance from the Asir region of Saudi Arabia. Performed at celebrations like weddings and in victory parades, it is a vibrant display of coordinated footwork and powerful vocalizations.'''
        }
        ,
        {
            "header":"The Qazou'i Performance",
            "body":'''The Qazou'i performance typically takes place in a semi-circular formation with two separate arched rows. A poet, or sometimes two or even four poets, stands in the center, engaging in a two-way, four-way, or six-way dialogue on a specific theme or topic. Each pair of poets exchanges verses, while one or two, three, or four, or even more individuals from the arranged rows regulate the movement by descending and stamping their feet. The central performer is referred to as the "muza'if" or "mahwiz." Among the Yaam tribes, the performance takes place in a continuous circle with minor variations in some movements.'''
                            },
        ]
    
    poets=[{
        "name":"Falah Al-Qarqah",
        "img":"images/flah.jpg",
        "city":"Abha"

    },
    {
        "name":"Muta'ab Al-Masfari",
        "img":"images/mutaib.jpg",
        "city":"njd"
    },
    {
        "name":"Abdullah bin Shayiq",
        "img":"images/abdullahshaiq.jpg",
        "city":"muzahimih"
    },
    {
       "name":"Mohammed bin ksla",
        "img":"images/binksla.jpg",
        "city":"Ahad Rafidah"
    },
    

    ]
    



    return render(request,"main/qazwai.html",context={"info":infos,"poets":poets})

def picture_view(request:HttpRequest)->render:
    with open ("C:/Users/saeed/python-cam-lab/UNIT-2-PROJECT/sauidArdah/main/static/picturesLibrary/pictures.json",'r',encoding='UTF-8') as file:
        poets=json.load(file)
    return render(request,"main/pictures.html",context={"objects":poets})

def about_view(request:HttpRequest)->render:
    infos=[
        
        {
        "header":"Our Inspiration",
        "body":'''I created this website to address the challenge of finding comprehensive information about Saudi Ardah. The scattered nature of available resources made research difficult, prompting me to develop a centralized platform where enthusiasts can easily access a wealth of knowledge on this rich cultural tradition.'''
        },
        {
            "header":"Our Goal",
            "body":'''This website aims to preserve and promote the rich tradition of Saudi Ardah by providing a comprehensive online resource. By documenting various Ardah styles, educating visitors about its history and techniques, and fostering a community of enthusiasts, we strive to ensure that this vibrant cultural art form continues to thrive for generations to come.'''
                },
                {
                    "header":"Our Vision",
                    "body":'''Our vision for this website extends beyond its current scope. We are committed to providing a comprehensive resource for all enthusiasts of Saudi Ardah. To this end, we have ambitious plans to expand our content and features. Our primary goal is to document and showcase the diverse range of Ardah styles found across Saudi Arabia, from the energetic rhythms of Najdi Ardah to the graceful movements of Southern Ardah. We aspire to create a virtual journey through the nation's rich cultural tapestry, highlighting the unique characteristics of each region's Ardah tradition. Additionally, we recognize the importance of preserving and passing on this art form to future generations. Therefore, we are developing a series of interactive tutorials that will break down the complex movements and rhythms of Ardah, making it accessible to learners of all levels.'''
                },
                {
                    "header":"Embark on Your Ardah Journey",
                    "body":'''We invite you to embark on a captivating journey through the world of Saudi Ardah. Explore the rich history, diverse styles, and passionate community that define this cherished cultural treasure. Whether you are a seasoned Ardah enthusiast or a curious newcomer, we hope our website provides valuable insights and inspiration. Together, let us celebrate and preserve the legacy of Saudi Ardah for generations to come.'''
                }
        ]
    return render(request,"main/about.html",context={"info":infos})

def contact_view(request:HttpRequest):
    return render(request,"main/contact.html")