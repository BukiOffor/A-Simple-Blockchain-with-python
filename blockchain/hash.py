import hashlib
import random
import datetime
import sys

phrase = 'This is a test to see how long it takes to hash'
counter, difficulty = 0, "0"
try:
    for i in range(int(sys.argv[1])):
        initialization = datetime.datetime.now()
        print(f"Attempting Hash {i+1}.................")
        while True:
            nonce = random.randint(0,99999999999999)
            hash = hashlib.sha256(repr(phrase+str(nonce)).encode()).hexdigest()
            if not str(hash).startswith(difficulty):
                counter+=1
                continue
            else:
                cracked = datetime.datetime.now()
                cracked_time1 = cracked - initialization
                seconds_in_day = 24 * 60 * 60
                cracked_time = divmod(cracked_time1.days * seconds_in_day + cracked_time1.seconds, 60)
                print(f"difficulty = {difficulty} \nThe number of tries was {counter} \nThe Succeeding nonce was {nonce} \nHash is {hash} \nTime to hash {cracked_time[0]} mins {cracked_time[1]}secs \n")
                difficulty += "0"
                break
        counter = 0
except ValueError:
    print("*****Range should be an interger******\n")


    
    