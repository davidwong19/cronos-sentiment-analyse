# Cronos Sentiment Analyse

Automation and final csv file: [Cronos Sentiment](https://github.com/Rehtsecp/Cronos-Sentiment.git)

This is an readme file, that will explain how to use the scripts we used to gather, transform and analyse our data.

**Technologies we used**
- Python
- MongoDB
- Power BI Desktop

*Why we chose these technologies?*
- Partly because we are already familiar with these technologies because of the use in some of our school courses.
- Programs are all free/open-source. :satisfied:
  
## 1. The use of scrapers to gather review data

[Download Python](https://www.python.org/downloads/)

We will be using Python for scraping some of the websites. So there will be some necessities before running the scripts to scrape these websites.
We used pip to install the packages.

For the LinkedIn scraper we used Selenium to scrape the webapplication. You will not only need to install the Selenium package. But you will need to webdrivers, according to your browser. More info: [Selenium with Python](https://selenium-python.readthedocs.io/)

- 	`pip install pandas`
-   `pip install googletrans`
-   `pip install requests`
-   `pip install beautifulsoup4`
-   `pip install selenium`
-   `pip install textblob`

### 1.2 Running the scripts
You can run the python script by navigating to the **automation folder**. You need to change the directory in the various '.bat' files to where your 'python.exe' is located.

## 2. sources used to create dataset 'reviews_cronos_groep.csv'

- indeed
- glassdoor
- googl maps review
- beyondgaming
- facebook

We made an scraper for Glassdoor and Indeed. sources like facebook, stepstone and  beyondgaming we used a chrome extention  called 'instant data scraper' 
and for the google maps review we used a site called 'https://botster.io/registration'.

## 3. folders

 1. code for datavisualisatie folder

in this map you will find:  

- `reviews_cronos_groep.csv`
- `reviews_cronos_groep5.csv`                        
- `sentiment analyse visualisatie.pbix`
- `sentiment_analyse.ipynb`

NOTE:Rating in the csv file is the opinoin of the person and  score is the score of the algoritme!
`reviews_cronos_groep.csv`:this is the csv file that is used in `sentiment_analyse.ipynb` and this csv file contains all reviews of cronos and the smaller companies under cronos
`sentiment_analyse.ipynb`: this file will create the csv file used for the `sentiment analyse visualisatie.pbix` the file that will be created is `reviews_cronos_groep5.csv`
