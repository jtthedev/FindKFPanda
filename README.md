# FindKFPanda

I added time.sleep to add a little suspense, and make the process feel more "real". 

While testing I used 192.168.1.1 as an IP and the city and state value returned None. I decided to incorporate that error into the story with:
 "while fkp.city == None and fkp.state == None:
        print('Uh oh. Looks like he\'s too fast for us! He got away!')
        break"
