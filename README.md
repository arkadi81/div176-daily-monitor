# SJA DIVISION 176 DAILY MONITOR

An interactive web application for the display of important information for brigade members of Saint John Ambulance's division 176 - Victoria, BC

## Current Capabilities

### weather-scraper
The script scraps short term and long term weather info relevant to the Victoria area and displays it on the web page

## Usage 
```shell
	$ python3 weather.py 
```


## TODO
- Add unit / e2e testing (when incorporated with webapp framework)
- Display duty information using div176.ca API, if provided.
- Currently scraping from weather.gc.ca using BeautifulSoup/Python. weather.gc.ca html markup contains no ids and is generally painful to work with. TODO either change source website or request API for easier access to data
- Record important information
- Modules are currently CLI only. Convert to web app via introduction of either django or flask 
- Add visualization as necessary (maybe for cumulative hours etc)
- Add ability to produce pdf reports

## Sources
- Web scraping and visualization in python using beautiful soup and pandas: https://www.dataquest.io/blog/web-scraping-tutorial-python/
- Pandas info can be found in unit 2 of Lynda's "Python for Data Science Essential Training" at
https://www.lynda.com/Python-tutorials/Filter-select-data/520233/601939-4.html?autoplay=true