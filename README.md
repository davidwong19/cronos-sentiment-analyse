# Cronos Sentiment Analyse

This is an readme file, that will explain how to use the scripts we used to gather, transform and analyse our data.

**Technologies we used**
- Python
- MongoDB
- Power BI Desktop

*Why we chose these technologies?*
- Partly because we are already familiar with these technologies because of the use in some of our school courses.
- Programs are all free/open-source. :sweat_smile:
  
## 1. The use of scrapers to gather review data

We will be using Python for scraping some of the websites. So there will be some necessities before running the scripts to scrape these websites.
We used pip to install the packages.

For some scrapers we used Selenium to scrape the webapplication. You will not only need to install the Selenium package. But you will need to webdrivers, according to your browser. More info: [Selenium with Python](https://selenium-python.readthedocs.io/)

- 	`pip install pandas`
-   `pip install googletrans`
-   `pip install requests`
-   `pip install beautifulsoup4`
-   `pip install selenium`