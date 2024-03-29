import os
from dotenv import load_dotenv
from flask import Flask, app, render_template, request
import pgeocode
from dotenv import load_dotenv
from googleplaces import GooglePlaces, types
import jinja2

load_dotenv()
API_KEY = os.getenv("GOOGLE_API")

app = Flask(__name__)
env = jinja2.Environment()
env.globals.update(zip=zip)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST", "GET"])
def search():
    postalCode = request.form["postalCode"]
    distance = request.form["distance"]

    # Google Places API Key
    google_places = GooglePlaces(API_KEY)

    # gets latitude and longitude from user input of postal code ONLY WORKS IN CANADA
    postal_code = postalCode  # gets postal code from the website
    nomi = pgeocode.Nominatim('ca')
    location = nomi.query_postal_code(postal_code)
    lat_long = location.latitude, location.longitude

    lat, long = lat_long

    query_result = google_places.nearby_search(
        lat_lng={'lat': lat, 'lng': long},
        # keyword='curbside pickup, delivery',
        keyword='Restaurants',
        radius=int(distance) * 1000,
        types=[types.TYPE_RESTAURANT]
    )

    if query_result.has_attributions:
        print(query_result.html_attributions)

    allNames = []
    allPhones = [] 
    allWeb = []

    for place in query_result.places:
        place.get_details()
        placeN = place.name
        placeL = place.local_phone_number
        placeW = place.website
        allNames.append(placeN)
        allPhones.append(placeL)
        allWeb.append(placeW)

    return render_template("search.html", postalCode=postalCode, distance=distance, allNames=allNames, allPhones=allPhones, allWeb=allWeb, zip=zip)


if __name__ == "__main__":
    app.run(debug=True)
