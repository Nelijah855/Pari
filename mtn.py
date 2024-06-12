import os
from mtnmomo.collection import Collection


class Mtn():
    
    client = Collection({
        "COLLECTION_USER_ID": os.environ.get("COLLECTION_USER_ID"),
        "COLLECTION_API_SECRET": os.environ.get("COLLECTION_API_SECRET"),
        "COLLECTION_PRIMARY_KEY": os.environ.get("COLLECTION_PRIMARY_KEY"),
    })

    
    
   
    
    def mtnpay(self):
        self.client.requestToPay(
    mobile="256772123456", amount="600", external_id="123456789", payee_note="ur too", payer_message="thanks", currency="ugx")



#d484a1f0d34f4301916d0f2c9e9106a2
#providerCallBackHost: https://akabbo.ug


"""
api user
"""

import uuid
reference_id = str(uuid.uuid4())
print(reference_id)


#

import httplib, urllib, base64
api_user = ""
api_key =""
api_user_and_key  = ""
encoded = base64.b64encode(api_user_and_key)
headers = {
    # Request headers
    'Authorization': 'Basic '+encoded,
    'Ocp-Apim-Subscription-Key': '<put-your-primary-subscription-id-here>',
}
params = urllib.urlencode({
})
try:
    conn = httplib.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/collection/token/?%s" % params, "{body}", headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


    #code to get 5000 from user account
    import httplib, urllib, base64, uuid,json
token = ''
reference_id = str(uuid.uuid4())
headers = {
    # Request headersi
    'Authorization': 'Bearer '+token,
    'X-Callback-Url': <replace with own http://myapp.com/momoapi/callback>,
    'X-Reference-Id': refrence_id,
    'X-Target-Environment': 'sandbox',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '<put-your-primary-subscription-id-here>',
}
params = urllib.urlencode({})
body = json.dumps({
  "amount": "5000",
  "currency": "UGX",
  "externalId": "12345",
  "payer": {
    "partyIdType": "MSISDN",
    "partyId": "0780123456"
  },
  "payerMessage": "test message",
  "payeeNote": "test note"
})
try:
    conn = httplib.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/collection/v1_0/requesttopay?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

    #https://parisx.000webhostapp.com/
    #https://parais123.000webhostapp.com/