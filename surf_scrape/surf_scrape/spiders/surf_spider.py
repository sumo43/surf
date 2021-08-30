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


    # TODO make this better
    # crawl outbound links up to this depth, to form a graph (hopefully)
    # depth 0-2 is already a lot of links, so that's all we're doing for now
    crawl_depth = 0

    # TODO figure out how to crawl external links only, maybe through rules?
    rules = (
        Rule(LinkExtractor(allow=('amazon',))),
        Rule(LinkExtractor(allow=('prime',)))
    )

    # a dict representing the connections between the urls
    urls = dict()

    def __init__(self):
        super(CrawlSpider, self).__init__()



    def start_requests(self):

        test_url = "https://google.com"

        self.push_url(test_url)

        yield scrapy.Request(url=test_url, callback=self.parse)

    # TODO figure out how to crawl external links only, maybe through rules?
    # TODO figure out how to crawl amazon + other sites with robots.txt
    # can use a proxy, or make it look like a real user somehow?
    # rate limit?

    def push_url(self, url):
        if(self.crawl_depth < 3 and url not in self.urls.keys()):
            yield scrapy.Request(
                url=url, 
                headers={'User-Agent': 'Mozilla/5.0'},
                usercallback=self.parse
            )
        else:
            self.crawl_depth = 0
            return

    def parse(self, response):
        self.logger.info("Currently on page: %s", response.url)

        source_url = response.url
        source_parser = urlparse(source_url)
        source_url_netloc = source_parser.netloc


        self.urls[source_url] = []

        out_links = []

        for a in response.xpath('//a/@href'):

            url = a.get()
            parser = urlparse(url)
            url_netloc = parser.netloc
            if(url_netloc != ''):
                # has a netloc

                # check if the url is "external" (includes local subdomains, e.g. maps.google.com)
                if(url_netloc != source_url_netloc):
                    full_url = parser.scheme + "://" + parser.netloc
                    out_links.append(full_url)

            else:
                # doesnt have a netloc
                print("doesnt have netloc: " + url)
        
        for link in out_links:
            # add the outbound link to the "graph"
            urls[source_url].append(link)

            # crawl the outbound link
            self.crawl_depth += 1
            push_url(link)

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
        
