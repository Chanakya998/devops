# Random 6 digit pin generation at 2 seconds interval

import random
import time
for i in range(5):
    print("OTP is valid for 2 sec")
    print(random.randint(100000,999999))
    time.sleep(2)