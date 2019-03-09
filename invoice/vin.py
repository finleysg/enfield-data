import json

import requests

search_url = "https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/{}?format=json"


def search_by_vin(vin):
    url = search_url.format(vin)
    response = requests.get(url)
    obj = json.loads(response.text)
    if obj is not None:
        d = obj.get("Results", None)[0]
        result = {
            "result_code": d.get("ErrorCode", None),
            "make": d.get("Make", "unknown"),
            "model": d.get("Model", "unknown"),
            "year": d.get("ModelYear", "0000")
        }
        return result
    return None

