
Table of Contents
=======================

* [What is surf?](#what-is-surf)
* [Running on Linux](#running-on-mac-os)
* [Running on PC](#running-on-linux)
* [Directory Structure](#directory-structure)
* [Contributing](#contributing)

------

What is surf?(WIP)
------

(WIP)

Running on Mac OS
------

```
./surf_install.sh
```

Running on Linux (WIP)
------

Directory Structure (WIP)
------
    
    ├── ext                 # Chrome / Firefox extensions for gathering searches
    ├── scrape              # web scraper, to run in background
    ├── docs                # Documentation (WIP)
    ├── ui                  # web / app UI (WIP)
    ├── logging             # logging
    └── messaging           # internal IPC messaging between components (WIP)



Contributing (WIP)
------

/Users/artem/Library/Application Support/Google/Chrome/NativeMessagingHosts

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

- Look into amazon s3 storage or fileserver to store the crawled data
- Look into what you want to store / what you need
    - name, desc of website
    - google analytics data of website through API?
    - Format (JSON, Table?)


# Web Crawler Pipeline
- Flask app calls Crawler
(Data from crawler) -> format_data.py -> matrix for pagerank -> mat.csv
                                      -> website metadata (later) -> meta.json
                                      -> schema.json for pagerank schema


   

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




