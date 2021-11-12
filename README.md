
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

Surf is a self-hosted search engine, which attempts to provide relevant search results based on pages similar to the ones you've already visited. Upon visiting a new webpage, the Surf web extension communicates the webpage to the surf back-end, which crawls the outbound links of the webpage and ranks them using
PageRank.

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
    ├── process_data        # python scripts for processing data (WIP)
    ├── logging             # logging web scraping + data processing(WIP)
    └── messaging           # internal IPC messaging between components (WIP)

Contributing (WIP)
------
# Web Crawler Pipeline
- crawler_handler script (running in backgroun) calls crawler:
(Data from crawler) -> format_data.py -> matrix for pagerank -> mat.csv
                                      -> website metadata (later) -> meta.json
                                      -> schema.json for pagerank schema


   



