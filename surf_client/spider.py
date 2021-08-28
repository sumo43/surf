import scrapy
import scrapy.spiders.crawlSpider as Spider
from urllib.parse import urlparse

class SurfSpider(Spider):
    name = "surf_spider"

    SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'
    CONCURRENT_REQUESTS = 100


    def start_requests(self):
        urls = []

    def push_request(self, url):
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        



        # parser = urlparse(url)
        # parser.netloc is same?
        
        


        


    def __init__(self):
        super()
        this.urls_list = []
