from flask import Flask, app, redirect, url_for, render_template, request
import pgeocode
import requests
from urllib.parse import urlencode

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST", "GET"])
def search():
    postalCode = request.form["postalCode"]
    distance = request.form["distance"]

    # Google Places API Key
    API_KEY = 'AIzaSyB9R7udTrzDh82n8EqzB9FcfcY9RMCxtK0'

    # gets latitude and longitude from user input of postal code ONLY WORKS IN CANADA
    postal_code =  postalCode   # needs input from webpage also
    nomi = pgeocode.Nominatim('ca')
    location = nomi.query_postal_code(postal_code)
    lat_long = location.latitude, location.longitude

    lat, long = lat_long
    print(lat, long)

    places_endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params_places = {
        "key": API_KEY,
        "location": f"{lat}, {long}",
        "radius":  distance ,  # needs input from the webiste
        "keyword": "curbside pickup",
        "types": "food"
    }
    params_places = urlencode(params_places)
    urlPlaces = f"{places_endpoint}?{params_places}"

    PlacesReq = requests.get(urlPlaces)
    # return the json instead of printing it
    print(PlacesReq.json())

    return render_template("search.html", postalCode=postalCode, distance=distance)


if __name__ == "__main__":
    app.run(debug=True)
