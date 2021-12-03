#request module for http request

import requests
# r=requests.get("https://www.google.com/search?q=ind+vs+nz&oq=&aqs=chrome.3.35i39i362l4j46i39i199i291i362j35i39i362l3.7653143j0j7&sourceid=chrome&ie=UTF-8")
# r=requests.get("https://en.wikipedia.org/wiki/Sachin_Tendulkar")
# print(r.text)

# url="http://www.wikipedia.com"
# data={"sachin tendulkar":1973}
# r2=requests.post(url=url,data=data)

URL = "http://maps.googleapis.com/maps/api/geocode/json"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address': location}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

# extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

# printing the output
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      % (latitude, longitude, formatted_address))