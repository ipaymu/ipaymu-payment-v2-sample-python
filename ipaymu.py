import requests
import json
from datetime import datetime
import hashlib
import hmac

ipaymuVa  = "1179000899" #your iPaymu VA
ipaymuKey = "QbGcoO0Qds9sQFDmY0MWg1Tq.xtuh1" #your iPaymu API Key
ipaymuUrl = "https://sandbox.ipaymu.com/api/v2/payment/direct" #production: https://my.ipaymu.com
body =  {
            "name":"Putu",
            "phone":"08123456789",
            "email":"putu@mail.com",
            "amount":"100000",
            "notifyUrl":"http://your-callback-url.com",
            "comments": "Payment to PT Demo",
            "referenceId": "1234", #your reference ID
            "paymentMethod": "va",
            "paymentChannel": "bca"
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
