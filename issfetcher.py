import requests

class IssFetcher:
    def __init__(self):
        self.base_url = "http://api.open-notify.org/iss-now.json"

    def fetch_iss(self):
        response = requests.get(self.base_url)
        response.raise_for_status()
        data = response.json()
        latitude=data["iss_position"]["latitude"]
        longitude=data["iss_position"]["longitude"]
        # iss_position=(latitude, longitude)
        return latitude,longitude


