__author__ = 'Nathan A. Smith'


from urllib.request import urlopen
from urllib.parse import quote
import json

location = input("Give Me A City and State (City, ST): ")
baseurl = 'https://query.yahooapis.com/v1/public/yql?'
yql_woeid = 'select woeid from geo.places where text=\"' + location + '\"'
yql_wx = 'select title, item from weather.forecast where woeid='


def get_yahoo_data(yql_query):
    yql_url = baseurl + 'q=' + quote(yql_query) + '&format=json'
    print(yql_url)
    result = urlopen(yql_url).read()
    result_str = result.decode('utf-8')
    data = json.loads(result_str)

    return data


def get_woeid():
    woeid_json = get_yahoo_data(yql_woeid)
    if woeid_json['query']['count'] == 1:
        local_woeid = woeid_json['query']['results']['place']['woeid']
    else:
        local_woeid = woeid_json['query']['results']['place'][0]['woeid']

    return local_woeid

woeid = get_woeid()
yql_wx += woeid
wx_data = get_yahoo_data(yql_wx)


print(wx_data['query']['results']['channel']['title'])
print('Current Conditions: ' + "\n" +
      "Temperature: " + wx_data['query']['results']['channel']['item']['condition']['temp'] + "\n"
      "Conditions: " + wx_data['query']['results']['channel']['item']['condition']['text'])
print(wx_data['query']['results']['channel']['item']['title'] + "\n" + "Forecast:")

for day in wx_data['query']['results']['channel']['item']['forecast']:
    print(day['day'] + ' High: ' + day['high'] + ' Low: ' + day['low'] + ' Forecast: ' + day['text'])
