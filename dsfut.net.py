import hashlib
import time
from datetime import datetime

import requests

fifa = ""  # Enter fifa version
console = ""  # Enter platform
partner_id = ""  # Enter your partner id
secret_key = ""  # Enter your secret key
##### Buy Now Price will be ckecked!!!!
min_buy_value = ""  # Enter minimum price
max_buy_value = ""  # Enter maximum price
take_after_value = "0"
timestamp = str(int(datetime.now().timestamp()))
pattern = partner_id + secret_key + timestamp
signature = hashlib.md5(pattern.encode()).hexdigest()


n = 0
while True:
    n += 1
    now = datetime.now().time()
    url = f"https://dsfut.net/api/{fifa}/{console}/{partner_id}/{timestamp}/{signature}?min_buy={min_buy_value}&max_buy={max_buy_value}&take_after={take_after_value}"
    end_time = time.time()
    r = requests.get(url)
    data = r.json()
    error = data["error"]
    if error == "throttle":
        print(data["message"])
        print(data, f"ReqNo.{n} {now}")
        break
    elif error == "":
        print(data["message"])
        print(data, f"ReqNo.{n} {now}")
        break
    else:
        print(data["message"])
        print(data, f"ReqNo.{n} {now}")

    time.sleep(1)
