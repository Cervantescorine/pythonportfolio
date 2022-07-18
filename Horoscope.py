# horoscope generator will require the random module

import random

# horoscope to user will be based upon their elemental sign pulled from lists

air_sign_prompt = [ ' Today is perfect for new endeavors.' , ' The tensions of this week will feel heavier today than yesterday.' , 
' Today is the day to cherish and embrace others. ' , ' Making yourself useful is a main component of a successful day.' , 
' Today, exercise caution when crossing the street.' ]

water_sign_prompt = [ ' Remember that good things come to those who work hard' , ' Don\'t let the circumstances bring you down.' ,
 ' Patience is key, but sometimes a little push can get the job done. ' , 
 ]

fire_sign_prompt = [ ' Looking ahead may seem like a waste of time, but it pays off in the end. ' , ' Luck favors those who mind the risks and take them' , 
 ' Today is the day for that thing you always wanted to do' ]

earth_sign_prompt = [ ' A smile can get you a long way. ' , ' Things are looking up for you. ' , 
' Luck is on your side today, so seize it!']

# number will help guarantee errors if user misspells their sign

print('1 - Aries')
print('2 - Taurus')
print('3 - Gemini')
print('4 - Cancer')
print('5 - Leo')
print('6 - Virgo')
print('7 - Libra')
print('8 - Scorpio')
print('9 - Sagittarius')
print('10 - Capricorn')
print('11 - Aquarius')
print('12 - Pisces')

# int makes what user inputs into a number and stores it into our variable "zodiac"
zodiac = int(input('Hello! Let\'s get your horoscope. Please pick your sign by typing the corresponding number and pressing Enter:  '))

# fire(1, 5, 9)     air(3, 7, 11)
# earth(2, 6, 10)   water(4, 8, 12) 

if 1 or 5 or 9: 
    print(random.choice(fire_sign_prompt))
elif 3 or 7 or 11: 
    print(random.choice(air_sign_prompt))
elif 2 or 6 or 10:
    print(random.choice(earth_sign_prompt))
elif 4 or 8 or 12: 
    print(random.choice(water_sign_prompt))
else: 
    print('Sorry, this isn\'t a corresponding number. Please try again.') 