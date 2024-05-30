import requests
from datetime import datetime

class SunTimesFetcher:
    def __init__(self, lat=34.125263, lng=241.958027, tzid="America/Los_Angeles"):
        self.lat = lat
        self.lng = lng
        self.tzid = tzid
        self.formatted = 0
        self.base_url = "https://api.sunrise-sunset.org/json"

    def fetch_sun_times(self):
        parameters={
            "lat": self.lat,
            "lng": self.lng,
            "tzid": self.tzid,
            "formatted":self.formatted,
            "date": "today",
        }
        response=requests.get(self.base_url, params=parameters)
        response.raise_for_status()
        data=response.json()['results']

        # astronomical_twilight_begin=data["astronomical_twilight_begin"]
        # astronomical_twilight_end=data["astronomical_twilight_end"]

        astronomical_twilight_begin=self.extract_hour_minute(data["astronomical_twilight_begin"])
        astronomical_twilight_end=self.extract_hour_minute(data["astronomical_twilight_end"])


        return astronomical_twilight_begin,astronomical_twilight_end

    @staticmethod
    def extract_hour_minute(time_str):
        a = datetime.fromisoformat(time_str)
        b = a.strftime("%H:%M")
        return b


# 创建类的实例并获取天文黎明和天文黄昏时间
# fetcher = SunTimesFetcher()
# astronomical_twilight_begin, astronomical_twilight_end = fetcher.fetch_sun_times()
# print("Astronomical Twilight Begin:", astronomical_twilight_begin)
# print("Astronomical Twilight End:", astronomical_twilight_end)
# #
# # 使用新的纬度、经度和时区创建实例
# fetcher = SunTimesFetcher(lat=34.052235, lng=118.243683, tzid="America/Los_Angeles")
# astronomical_twilight_begin, astronomical_twilight_end = fetcher.fetch_sun_times()
#
# print("Astronomical Twilight Begin:", astronomical_twilight_begin)
# print("Astronomical Twilight End:", astronomical_twilight_end)





