# Start Here

Installing Needed Packages
This particular web scrapy is been powered by "scrapy", an open-source web crawling framework
To implement this web scrapper install it into your environment by using the command below

       pip install scrapy

To Scrap the Specific Pages
Following web scraping best practices, different spiders have been created to meet the needs of different categories with regards the peculiarities of their web pages and pagination of each category...

The scrapper was used on an online store to scrape prices

# Example Tutorial to scrape information from the boots category
1.cd into the project(Getting into the file location of the marcus scrapper in your terminal)

2. run "scrapy crawl marcus_boots" in the terminal, to crawl through the specified category in  
   the spider

3. And also to output in json
   run "scrapy crawl marcus_boots -o boots.json"
   Or for csv format
   run "scrapy crawl marcus_boots -o boots.csv"

P.S.
run "scrapy crawl YOUR_SPECIFIED_CATEGORY"

The data that will be crawled includes
1.shoeType(e.g boots)
2.shoeBrand
3.shoeName
4.price(Original price of shoe)
5.salePrice(Discounted price of some specific shoes)

30th of July, 2020 update
2 new files have been added to the project for review(The data scraped by marcus_boots.py was used as an example(boots.csv))
format.py
The first is the format.py to format whatever out we get from the crawler
(the result is an output.csv file)

Final_Format.ipynb
This converts the formatted file into a table that can be used for analysis
An example is already showed in the "Final_Format" notebook
