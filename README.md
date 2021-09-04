# Surf Pi client

util.py
- Url data structure for URL
    - figure out which metadata you want
    - make this a dictionary, which will go into our list later
    - figure out format

    - RANKING - non query ranking - PageRank? - assign this later 

- Store object 
    - Just a list for now
    - Future: implement priority queue for the ranking to display on server homepage
    - Future: implement lambda sort by ranking

server.py
    - add good post request that handles the utils and sends them back to the client



# Web Crawler

    Scrapy Web Crawler, run through github workflow later

    Hour Session
- Attempt to use signals to debug the crawler, get it to work
    - built in support for robots.txt, user-agent spoofing
- Look into amazon s3 storage or fileserver to store the crawled data
- Look into what you want to store / what you need
    - name, desc of website
    - google analytics data of website through API?
    - Format (JSON, Table?)

   

    Bonus Features
    - Option to crawl sitemap for faster crawling


# SQL server on Pi

- Implement schema for SQL server
- Add sites to the SQL server as they get added, adjust their visit count
- Implement pagerank on a sql server
- Implement search by keyword




# PageRank

- Figure out how to tie this to sql server


FUTURE: one script that sets everything up 




