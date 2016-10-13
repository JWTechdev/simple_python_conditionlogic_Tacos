# The Taco Formula
number_of_nachos = int(input('How Many Nachos Will You Eat?'))
day_of_week = input('What Day of The Week Will You Grub on Tacos?')
will_you_use_hotsauce_Yazz_Nah = input('Will You Use Hot Sauce?')

if will_you_use_hotsauce_Yazz_Nah == 'Yes':
    print('Go Home Its Over Already')
else:
    # You Have Made It This Far! Will you
    if number_of_nachos < 3 or day_of_week == 'Friday' or day_of_week == 'Saturday':
        print('Man Your Responsiblle, Your Hired')
    if number_of_nachos >= 3 or day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Sunday':
        print('We Found Someone Else, You Are Not Safe')
    else:
        print('Eat Some Celery Punk')
