import bs4
import pgeocode
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

# Google Places API Key
API_KEY = 'AIzaSyB9R7udTrzDh82n8EqzB9FcfcY9RMCxtK0'

# Use webscrapping to get the postal code and distance from the website and run the py program to get it working

page = requests.get()
# url_contents = requests.get(http://localhost/winhacks/search.html) 
soup = bs4.BeautifulSoup(page.content, "html.parser")
postalCode = soup.find("span", {"id": "result-postalCode"})
distanceRaduis = soup.find("span", {"id": "result-distance"})

# gets latitude and longitude from user input of postal code ONLY WORKS IN CANADA
postal_code = postalCode  # needs input from webpage also
nomi = pgeocode.Nominatim('ca')
location = nomi.query_postal_code(postal_code)
lat_long = location.latitude, location.longitude

lat, long = lat_long
print(lat, long)

places_endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
params_places = {
    "key": API_KEY,
    "location": f"{lat}, {long}",
    "radius": distanceRaduis,  # needs input from the webiste
    "keyword": "curbside pickup",
    "types": "food"
}
params_places = urlencode(params_places)
urlPlaces = f"{places_endpoint}?{params_places}"

PlacesReq = requests.get(urlPlaces)
print(PlacesReq.json())
print(postal_code)
