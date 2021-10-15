crawl
------

Web Crawler
- given a webpage, crawls web pages within three degrees of separation from the given web page
- Uses scrapy python framework

TODO
- parse second-degree domain names (eg. photos.google.com instead of google.com) as separate web pages, or sub-pages of a main page (google.com)
- figiure out why certain websites aren't being crawled (blocked?)
- add some kind of listener for sending/receiving data through IPC/similar (WIP)
- develop pipeline for web crawler using scrapy pipelines or similar

Web Crawler Pipeline
- crawler_handler script (running in background) calls crawler:
(Data from crawler) -> format_data.py -> numpy matrix for pagerank -> matrix.csv
                                      -> website metadata (later) -> meta.json
                                      -> schema.json for pagerank schema (remember indices of certain sites)



