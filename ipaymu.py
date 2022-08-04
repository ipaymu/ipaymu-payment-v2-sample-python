import requests
import json
from datetime import datetime
import hashlib
import hmac

ipaymuVa  = "1179000899" #your iPaymu VA
ipaymuKey = "QbGcoO0Qds9sQFDmY0MWg1Tq.xtuh1" #your iPaymu API Key
ipaymuUrl = "https://sandbox.ipaymu.com/api/v2/payment" #production: https://my.ipaymu.com
body =  {
            "product":["Jacket"],
            "qty":["1"],
            "price": ["150000"],
            "amount":"10000",
            "returnUrl":"https://your-website.com/thank-you-page", #your thank you page url
            "cancelUrl":"https://your-website.com/cancel-page", #your cancel page url
            "notifyUrl":"https://your-website.com/callback-url", #your callback url
            "referenceId":"1234", #your reference id or transaction id
            "buyerName":"Customer Name", #optional
            "buyerPhone":"08123456789", #optional
            "buyerEmail":"buyer@mail.com", #optional
        } 

data_body    = json.dumps(body)
data_body    = json.dumps(body, separators=(',', ':'))
encrypt_body = hashlib.sha256(data_body.encode()).hexdigest()
stringtosign = "{}:{}:{}:{}".format("POST", ipaymuVa, encrypt_body, ipaymuKey)
signature    = hmac.new(ipaymuKey.encode(), stringtosign.encode(), hashlib.sha256).hexdigest().lower()

timestamp    = datetime.today().strftime('%Y%m%d%H%M%S')

headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'signature': signature,
    'va':ipaymuVa,
    'timestamp':timestamp
}
response = requests.post(ipaymuUrl, headers=headers, data=data_body)

print(response.text)