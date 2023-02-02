import httpx
import json

with httpx.Client() as client:
    response = client.get('https://t4.tc.columbia.edu/ajax/courses-v2.php?callback=jsonp__callback&page=1&jsonp=true&termCode=W23&_=1675373819781')
print(response.content.replace('\',))
# js = json.loads(response.text.replace('\'', '\\'
# print(js)


