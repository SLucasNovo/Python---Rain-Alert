import requests
from twilio.rest import Client

API_KEY = os.environ.get('api_key')
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
WEATHER_URL = os.environ.get('weather_url')
TWILLIO_PHONE_NUMBER = os.environ.get('tw_num')
MY_PHONE_NUMBER = os.environ.get('number')

MY_PARAMETERS = {
    # 'q': 'City,Country',
    'appid': API_KEY
    , 'lat': lat,
    'lon': lon
    , 'exclude': "current,minutely,daily"
    #, 'formatted': 0
}

response = requests.get(url='WEATHER_URL ', params=MY_PARAMETERS)
response.raise_for_status()
weather_data = response.json()

will_rain = False

hourly_id_list = []


for i in range(0, 12):
    hourly_data = weather_data['hourly'][i]['weather'][0]['id']
    hourly_id_list.append(hourly_data)
    if hourly_data < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="It's going to rain. Use an ☂️",
        from_= TWILLIO_PHONE_NUMBER ,
        to=MY_PHONE_NUMBER 
    )

    print(message.status)



