from sunset import SunTimesFetcher
from issfetcher import IssFetcher
from datetime import datetime, time
import smtplib
from email.mime.text import MIMEText

from my_config import EMAIL_CONFIG

MY_LAT=34.125263
MY_LONG=241.958027

# MY_LAT=lat=-37.125263
# MY_LONG=lng=-79.958027

my_email = EMAIL_CONFIG['my_email']
password = EMAIL_CONFIG['password']
to_email = EMAIL_CONFIG['to_email']



fetcher = SunTimesFetcher()
astronomical_twilight_begin, astronomical_twilight_end = fetcher.fetch_sun_times()
start_time = astronomical_twilight_end
end_time = astronomical_twilight_begin

def check_lat_long():
    issfetch=IssFetcher()
    latitude, lngitude=issfetch.fetch_iss()
    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= lngitude <= MY_LONG + 5:
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

    # 创建邮件消息对象，并指定字符集编码为 UTF-8
    msg=MIMEText("当前ISS正在你的上空，并且天空足够暗，请抬头观看。", _charset="utf-8")
    msg['Subject']="当前ISS正在你的上空"
    msg['From']=my_email
    msg['To']=to_email

    # 连接 SMTP 服务器并发送邮件
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.send_message(msg)

else:
    print("当前ISS不在你的上空，跳过。")
    # 在这里放置跳过的逻辑
