"""
As a user I want to be able to enter my city or zip code
and recieve my temp in C or F.

As a user I want to know what condition it is outside.
"""

import requests

package = {
    'APPID': "9ef3311b380d2586bf47ff522529e7a9",
    'q': 'London'
}

r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)

json_data = r.json()

print(r.url)
print(json_data)
