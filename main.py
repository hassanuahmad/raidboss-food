from flask import Flask, app, redirect, url_for, render_template, request
import pgeocode
import requests
from urllib.parse import urlencode
from googleplaces import GooglePlaces, types, lang

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
    google_places = GooglePlaces(API_KEY)

    # gets latitude and longitude from user input of postal code ONLY WORKS IN CANADA
    postal_code = postalCode  # gets postal code from the website
    nomi = pgeocode.Nominatim('ca')
    location = nomi.query_postal_code(postal_code)
    lat_long = location.latitude, location.longitude

    lat, long = lat_long

    query_result = google_places.nearby_search(
        lat_lng={'lat': lat, 'lng': long},
        keyword='curbside pickup',
        radius=int(distance) * 1000,
        types=[types.TYPE_RESTAURANT]
    )

    if query_result.has_attributions:
        print(query_result.html_attributions)

    allPlaces = []
    for place in query_result.places:
        place.get_details()
        # print(place.name)
        # print(place.local_phone_number)
        # print(place.website)
        placeN = place.name
        placeL = place.local_phone_number
        placeW = place.website
        allPlaces.append(placeN)
        allPlaces.append(placeL)
        allPlaces.append(placeW)

    return render_template("search.html", postalCode=postalCode, distance=distance, allPlaces=allPlaces)


if __name__ == "__main__":
    app.run(debug=True)
