#first attempt at python programming, file access, analysis
# based on seng265 assignment
import os
import sys
import inspect
# from datetime import datetime
import requests #required to shoot get reqs to webpages to download html content
from bs4 import BeautifulSoup #needed to parse the stuff we get from requests
import pandas as pd # data analysis tools
import re

# included from https://stackoverflow.com/questions/6810999/how-to-determine-file-function-and-line-number/6811020
# implements __LINE__ functionality for debugging, as in c++
# requires import sys
class __LINE__(object):
    def __repr__(self):
        try:
            raise Exception
        except:
            return str(sys.exc_info()[2].tb_frame.f_back.f_lineno)

__LINE__ = __LINE__()
# END line functionality

# url = "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"

def weather_gc_ca_scraper():
	url = "https://weather.gc.ca/city/pages/bc-85_metric_e.html" # victoria

	page = requests.get(url)
	soup = BeautifulSoup(page.content,"html.parser")

	temps = soup.find_all(class_="high wxo-metric-hide")[:6]
	# print(type(temps))
	# print(temps)
	headers = soup.find_all(class_="div-row div-row1 div-row-head")
	# print(headers)
	# print(headers[0])

	# print(dir(headers))
	week_days = [h.find_all("strong")[0].get_text() for h in headers]
	dates = [h.find_all("br")[0].get_text() for h in headers]

	#-------------
	print("Current 6 day forcast in Victoria, BC, based on weather.gc.ca")
	print(week_days)
	# print(dates)
	print([re.search("(\d+)",d).group(0) for d in dates]) # extract numerical date
	print([re.search("(\d+)\xa0(\w{3})",d).group(2) for d in dates]) # extract month
	print([int(re.search("\d+",t.get_text()).group(0)) for t in temps])

	# print(type(headers))
	# print(headers)
	# print(type(headers[0]))
	# print(headers[0])
	# print(type(h2))
	# print(h2)
	# print([h for h in headers.find('abbr')])



def main():
	page = requests.get(url)
	# print(page.content)
	soup = BeautifulSoup(page.content,"html.parser")
	# print(soup.prettify())
	# print([type(item) for item in list(soup.children)])
	# seven_day = soup.find(id="seven-day-forecast") #we must know the html structure through webdev tools to know the exact name
	# print(type(seven_day))
	# forecast_items = seven_day.find_all(class_="tombstone-container")

	#more efficient use - comprehensions
	# period_tags = seven_day.select(".tombstone-container .period-name")
	# periods = [pt.get_text() for pt in period_tags]

	# short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
	# temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
	# descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

	# print(periods)
	# print(short_descs)
	# print(temps)
	# print(descs)
	# print(list(html.children))
	# for item in forecast_items:
	# 	period = item.find(class_="period-name").get_text()
	# 	short_desc = item.find(class_="short-desc").get_text()
	# 	temp = item.find(class_="temp").get_text()
	# 	# print(item.prettify())
	# 	# print(period,short_desc,temp)
	# 	pass
	# # print(soup.find_all('p'))
	# weather = pd.DataFrame({"period": periods,"short_desc": short_descs,"temp": temps,"desc":descs})
	# type(weather)
	# print(weather)
	# print(weather)
	# temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)")
	# weather["temp_num"] = temp_nums.astype('int')
	# print(weather["temp_num"])

	# SCRAPE WEATHER.GC.CA
	

if __name__ == "__main__":
	# main()
	weather_gc_ca_scraper()
