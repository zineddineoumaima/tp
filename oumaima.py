from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from dotenv import load_dotenv

import os
load_dotenv()  
#environment variables
APIKEY = os.getenv("APIKEY")
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '97',
    'limit': '1',


}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': APIKEY,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    json_string = json.dumps(data['data'])
    
    print(json_string)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

