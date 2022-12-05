
import datetime
from builtins import print

today = datetime.date.today()
print('today is ', today)

from datetime import date,timedelta
today = date.today()
print('today is ', today)

# 날짜 구하기
print("년도 : ", today.year)
print("년도 : ", today.month)

day=['월','화']
print("년도 : ", day[today.weekday()])

#날짜 계산
print('어제 :', today + timedelta(days=-1))
# 일주일전 날짜
print('어제 :', today + timedelta(weeks=-1))
# 10일 후 날짜
print('어제 :', today + timedelta(days=10))

from datetime import datetime
day = datetime.today()
print(day)

import datetime
day = datetime.datetime.today()
print(today)

#날짜를 문자열 형태 (strftime() 이용) (대소문자 구별)
print(day.strftime('%Y년 %m월 %d일 %H:%S'))
# 문자열을 날짜형태 (strptime() 이용)
naljja = '2022-12-25 12:50:59'
print(type(naljja))
mydate = datetime.datetime.strptime()
print(mydate)
print(type(mydate))