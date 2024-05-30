from sunset import SunTimesFetcher
from issfetcher import IssFetcher
from datetime import datetime, time

# lat=34.125263
# lng=241.958027

MY_LAT=lat=-37.125263
MY_LONG=lng=-79.958027
#can_lat = 30-40
#can_lng = 235-247

fetcher = SunTimesFetcher()
astronomical_twilight_begin, astronomical_twilight_end = fetcher.fetch_sun_times()

print("Astronomical Twilight Begin:", astronomical_twilight_begin)
print("Astronomical Twilight End:", astronomical_twilight_end)
start_time = astronomical_twilight_end
end_time = astronomical_twilight_begin
# 示例时间段
# start_time="21:11"
# end_time="05:39"



def check_lat_long():
    issfetch=IssFetcher()
    latitude, lngitude=issfetch.fetch_iss()
    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT - 55 <= latitude <= MY_LAT + 55 and MY_LONG - 55 <= lngitude <= MY_LONG + 55:
        return True
    else:
        return False







def is_within_time_range(start_time_str, end_time_str):
    # 获取当前时间
    now=datetime.now().time()
    # print(now)
    # 解析开始时间和结束时间字符串
    start_time=datetime.strptime(start_time_str, '%H:%M').time()
    end_time=datetime.strptime(end_time_str, '%H:%M').time()

    if start_time < end_time:
        # 时间段在同一天内
        return start_time <= now <= end_time
    else:
        # 时间段跨越午夜
        return now >= start_time or now <= end_time



if is_within_time_range(start_time, end_time) and check_lat_long :
    print("当前ISS正在你的上空，并且天空足够暗，执行程序。")
    # 在这里放置需要运行的程序代码
else:
    print("当前ISS不在你的上空，跳过。")
    # 在这里放置跳过的逻辑
