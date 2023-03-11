import time
start_time = time.time()
from datetime import datetime
import calendar
import requests
import hashlib
import time
import os
import winsound
from colorama import init, Fore
init()
#os.system("CLS")
n = 0
fifa = "" # Enter fifa version
console = "" # Enter platform
partner_id = "" # Enter your partner id
secret_key = "8dd2f198b0bf072ee93188cea3b5a77f" # Enter your secret key
##### Buy Now Price will be ckecked!!!!
min_buy_value = "" # Enter minimum price
max_buy_value = "" # Enter maximum price
take_after_value = "0"
message = "popped"
# d = datetime.utcnow()
# unixtime = str(calendar.timegm(d.utctimetuple()))
# print(unixtime)
# 1634835812
1634839922
t = "1000000000"
signature = partner_id + secret_key + t
result = hashlib.md5(signature.encode()).hexdigest()

while True:
    n += 1
    now = datetime.now().time()
    url = f"https://dsfut.net/api/{fifa}/{console}/{partner_id}/{t}/{result}?min_buy={min_buy_value}&max_buy={max_buy_value}"
    end_time = time.time()
    print(start_time,end_time,end_time-start_time)
    r = requests.get(url)
    
    # print(r.json())
    # print(type())
    if message not in str(r.content):
        print(Fore.RED + str(r.content) + "ReqNo."+ str(n), now)
    else:
        print(Fore.GREEN + str(r.content) + "ReqNo."+ str(n),now)
        f = open ('C:\\report.txt' , 'a')
        f.write(str(r.content) + "ReqNo."+ str(n) + '   ' + str(now))
        f.writelines('\n')
        f.close()
        # #winsound.Beep(1000, 10000)
        break
    time.sleep(0.334)