
Table of Contents
=======================

* [What is surf?](#what-is-surf)
* [Running on Linux](#setup-on-mac-os)
* [Running on PC](#setup-on-linux)
* [Directory Structure](#directory-structure)
* [Contributing](#contributing)

------

What is surf?(WIP)
------

Surf is a self-hosted search engine, which attempts to provide relevant search results based on pages similar to the ones you've already visited. Upon visiting a new webpage, the Surf web extension communicates the webpage to the surf back-end, which crawls the outbound links of the webpage and ranks them with PageRank.

Setup on Mac OS
------

```
./surf_install_macos.sh
```

Running on Linux (WIP)
------

```
./surf_install_linux.sh
```

Directory Structure (WIP)
------
    
    ├── ext                 # Chrome / Firefox extensions for gathering searches
    ├── crawl               # web crawler, to run in background
    ├── docs                # Documentation (WIP)
    ├── ui                  # web / app UI (WIP)
    ├── data                # data folder for web crawler data. Can move this somewhere else upon install
    ├── process_data        # python scripts for processing data (pagerank)
    ├── logging             # logging web scraping + data processing(WIP)
    └── messaging           # internal IPC messaging between components (WIP)

Contributing (WIP)
------

- Store object 
    - Just a list for now
    - Future: implement priority queue for the ranking to display on server homepage
    - Future: implement lambda sort by ranking

server.py
    - add good post request that handles the utils and sends them back to the client


# Web Crawler

    Scrapy Web Crawler, run through github workflow later

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




