from flask import Flask, request,jsonify

app = Flask(__name__)

trips=[
    {"id":1,"destination":"Pariz","price":350},
    {"id":2,"destination":"Rim","price":400},
    {"id":1,"destination":"Lisabon","price":450}
]

@app.route('/trips')
def show_trips():
    return json.dumps(trips)

@app.route('/trips/search')
def search_trips():
    destination = request.args.get('destination')
    for trip in trips:
        if trip['destination'] == destination:
            return jsonify(trip)
    return "No trip found"

@app.route('/book',methods=['POST'])
def book_trip():
    json = request.get_json()
    found_trip = None
    for trip in trips:
        if trip['id'] == json['trip_id']:
            found_trip = trip
    if not found_trip:
        return "Invalid trip id"

    message = f"Zajazd do {found_trip["destination"]} pre {json["people"]} osoby uspesne rezervovany pre {json["name"]}. Cena spolu {json["people"] * found_trip["price"]}€"
    return message

if __name__ == '__main__':
    app.run()
