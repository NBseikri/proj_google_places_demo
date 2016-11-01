from flask import Flask, render_template, jsonify, request
import requests
from key import key

app = Flask(__name__)

search_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
details_url = 'https://maps.googleapis.com/maps/api/place/details/json'
auto_url = 'https://maps.googleapis.com/maps/api/place/queryautocomplete/json'

@app.route('/')
def search_form():
    """Prompts user for search term"""

    return render_template('home.html')

@app.route('/places_search', methods=['GET'])
def search_results():
    """Runs Google Places query and returns jsonified search results"""

    # payload = {
    #     'key': key,
    #     'query': request.args.get('search')
    # }

    # # places search payload
    # search_req = requests.get(search_url, params=payload)
    # # type(search_req) == <class 'requests.models.Response'>
    # search_json = search_req.json()
    # # type(search_json) == <type 'dict'>
    # results = search_json.get('results')
    # results_dict = results[0]
    # placeid = results_dict.get('place_id')

    auto_payload = {
        'key' : key, 
        'input' : request.args.get('search')
    }

    auto_req = requests.get(auto_url, params=auto_payload)
    auto_json = auto_req.json()


    id_payload = {
        'key' : key,
        'placeid' : placeid
    }

    # places details payload using placeid from places search 
    details_req = requests.get(details_url, params=id_payload)
    details_json = details_req.json()

    return jsonify(auto_json)
    # I jsonified the places details just so I could see it in the browser
    # I want to create something else to render in the return line (a diff
    # template)

# ATTEMPTING TO GET MAP TO RENDER USING LAT LONG IN MAP.HTML
# @app.route('/map', methods=['GET'])
# def show_map():
#
#     return render_template ('map.html')

if __name__ == "__main__":
        app.debug = True
        app.run(host="0.0.0.0")