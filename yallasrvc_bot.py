import os
import telebot
# API_KEY="5832988010:AAEp9d-tymHeiV7SsKpRoxkj6toKvnHIuE8"
# API_KEY="5558711270:AAHIglw6ZVYERqj7Jt-jsLPKyFY94msXXFo"

API_KEY='6239324931:AAGt2JngWrgwxZWGB-dC_7EdZqX4x4HYp0g'
# API_KEY=os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message,"hey! how it is going..")
@bot.message_handler(commands=['hello'])
def greet(message):
    bot.reply_to(message,"Hello....chaitanya reddy")
# @bot.message_handler(commands=['start'])
# def greet(message):
#     bot.reply_to(message,"""Hello
#                         click the button or reply with your choice :
#                             1./bank
#                             2./card
#                             3.pay
#                             4./account
#                             5./simswap
#                             6./pgp
#                             7./cardotp
#                             8./callcenter
#                             9./ssn
#                             10./apple
#                             11./link""")


@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message,"""
            Hello Guys Welcome to 
                Yalla's food reciepes
                    Youtube Channel..........
        click the button or reply with your choice :
            1./nonvegcurry_items
            2./muttoncurry
            3./pappu
            4./pachadi
            5./natukodi_pulsu
            6./veg_recipies
            7./pickles
            8./nonveg_fryrecipies
            9./snack_items
            10./sweet_items
            11./pulihora
            12./chutney
            13./pindivantalu""")


@bot.message_handler(commands=['nonvegcurry_items'])
def greet(message):
    bot.reply_to(message,""" To get  nonvegcurry_items click the below link:
        https://www.youtube.com/watch?v=j1GVUaT3wAw&list=PLYzW_Q-anwtxSjKnx04uz_IfWft6hc2aI""")



@bot.message_handler(commands=['muttoncurry'])
def greet(message):
    bot.reply_to(message,"""To get  muttoncurry click the below link:    
    https://www.youtube.com/watch?v=KH1K2085KXc&list=PLYzW_Q-anwtxSjKnx04uz_IfWft6hc2aI&index=8""")


@bot.message_handler(commands=['pappu'])
def greet(message):
    bot.reply_to(message,"""click the below link to get pappu :
   https://www.youtube.com/playlist?list=PLYzW_Q-anwtzAt23-cCnCKnA_kxSI9Fxn  """)


@bot.message_handler(commands=['rasam_items'])
def greet(message):
    bot.reply_to(message,"""click the below link to get 
                 rasam_items:
    https://www.youtube.com/playlist?list=PLYzW_Q-anwtweuOl1ZFZOptTlxsNkHkTK""")


@bot.message_handler(commands=['natukodi_pulsu'])
def greet(message):
    bot.reply_to(message,"""click the below link to get 
    natukodi_pulsu:
    https://www.youtube.com/watch?v=j1GVUaT3wAw&list=PLYzW_Q-anwtxSjKnx04uz_IfWft6hc2aI&index=1""")


@bot.message_handler(commands=['veg_recipies'])
def greet(message):
    bot.reply_to(message,"""click the below link to get 
    veg_recipies:
    https://www.youtube.com/playlist?list=PLYzW_Q-anwty-NKlaw2o6XUbvze-qrCZX""")


@bot.message_handler(commands=['pickles'])
def greet(message):
    bot.reply_to(message,"""click the below link to get 
    pickles:
    https://www.youtube.com/watch?v=gNzlVTLmyH4&list=PLYzW_Q-anwtyLZlaLAqOpFVCgkO5EQ4ze""")


@bot.message_handler(commands=['nonveg_fryrecipies'])
def greet(message):
    bot.reply_to(message,"""click the below link to get 
    nonveg_fryrecipies: https://www.youtube.com/playlist?list=PLYzW_Q-anwty9NmwTT5TPjeBBGo3G6FvA
 """)


@bot.message_handler(commands=['snack_items'])
def greet(message):
    bot.reply_to(message,""" hello welcome ... click the below link  

                To get the snack_items:

            https://www.youtube.com/playlist?list=PLYzW_Q-anwtwhT5c6uY_Ztsd1EryaA49X
     """)
@bot.message_handler(commands=['sweet_items'])
def greet(message):
    bot.reply_to(message,""" hello welcome ... click the below link  

                To get the sweet_items item:

                https://www.youtube.com/playlist?list=PLYzW_Q-anwtzsxQ2nT-shCqM_N29kFKec
     """)


@bot.message_handler(commands=['pulihora'])
def greet(message):
    bot.reply_to(message,""" hello welcome ... click the below link  

                To get the pulihora item:

                https://www.youtube.com/playlist?list=PLYzW_Q-anwtz_zwEO0ihjVOPPIZkkkuXd
     """)
    
@bot.message_handler(commands=['chutney'])
def greet(message):
    bot.reply_to(message,""" hello welcome ... click the below link  

                To get the chutney item:

                https://www.youtube.com/playlist?list=PLYzW_Q-anwtxbOvvFGqeTePjQBSdLY4jc
     """)
@bot.message_handler(commands=['pindivantalu'])
def greet(message):
    bot.reply_to(message,""" hello welcome ... click the below link  

                To get the pindivantalu item:

                https://www.youtube.com/playlist?list=PLYzW_Q-anwtyhesWMoiSMeOLpXcAsurB1
     """)
bot.polling()