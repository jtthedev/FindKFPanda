#Where is Kung-fu Panda?
#This is a practice program I wrote in Python to perform IP look ups.
#I got the idea from the "Where is Santa?" app

import geocoder
import time

def find_panda():
    print(' Where is Kung-Fu Panda?!')
    fkp = geocoder.ip(input('Enter IP address: '))
    time.sleep(2)
    print(' I may have found him!')
    time.sleep(1)
    print('Kung-Fu Panda apears to be in ' + str(fkp.city) + ' ' + str(fkp.state))
    
    while fkp.city == None and fkp.state == None:
        print('Uh oh. Looks like he\'s too fast for us! He got away!')
        break
    while True:
        a1 = input('Would you like more info? ')
        if a1.lower() == 'yes': 
            if a1.lower() == 'yes' and fkp.city == None and fkp.state == None:
                print('He\'s a big fella, but he has hands! He beat up our ninja!')
                break
            else:
                print('Panda is at ' + str(fkp.latlng) )
                break
        elif a1.lower() == 'no' :
                print(' Ok Then! Have fun with Panda!')
                break
        if a1.lower() != 'yes' or 'no':
            print(' Sorry Friend. That\'s not one of the choices... Yes or No only!')


find_panda()
