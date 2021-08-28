import scrapy
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

class SurfSpider(CrawlSpider):

    name = "surf_spider"

    # config for spider that only crawls external links
    SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'
    CONCURRENT_REQUESTS = 100

    # TODO figure out how to crawl external links only, maybe through rules?
    rules = (
        Rule(LinkExtractor(allow=('amazon',))),
        Rule(LinkExtractor(allow=('prime',)))
    )

    urls = []

    def __init__(self):
        super(CrawlSpider, self).__init__()

        self.urls.append("https://microsoft.com")


    def start_requests(self):

        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def push_url(self, url):
        print("push url called")
        current_url = url
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info("Currently on page: %s", response.url)

        print("response xpath")
        print(response.xpath('//a'))
        

    def get_cache(self):
        return self._cache

        # parser = urlparse(url)
        # parser.netloc is same?


if __name__ == "__main__":
    test_cache = dict()
    test_cache['amazon.com'] = []
    process = CrawlerProcess( {
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    })
    process.crawl(SurfSpider, dict())
    process.start()
        
