import scrapy
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy import signals

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

    MAX_DEPTH = 3
    
    # a dict representing the connections between the urls
    urls = dict()

    def __init__(self):
        print("spider initialized")


    def error_handler(self, err):
        print("an error happened")


    def start_requests(self):

        test_url = "www.facebook.com"

        self.urls[test_url] = dict()
        self.initialize_data(test_url, 0)

        yield scrapy.Request(
            url=self.unparse(test_url), 
            headers = {'User-Agent': 'Mozilla/5.0'},
            callback=self.parse,
            errback=self.error_handler
        )

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(SurfSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)

    def spider_closed(self, spider):
        spider.logger.info("spider closed, bottom text")
        self.crawler_finished()
        


    # TODO figure out how to crawl external links only, maybe through rules?
    # TODO figure out how to crawl amazon + other sites with robots.txt
    # can use a proxy, or make it look like a real user somehow?
    # rate limit?

    def crawl_url(self, url):
        if(self.urls[url]['depth'] < 3):
            yield scrapy.Request(
                url=url, 
                headers={'User-Agent': 'Mozilla/5.0'},
                callback=self.parse,
                errback=self.error_handler
            )
        else:
            print("maximum crawl depth exceeded")
            self.crawl_depth = 0
            return
    

    def parse(self, response):

        # parse the source url...
        source_url = response.url
        source_parser = urlparse(source_url)
        source_url_netloc = source_parser.netloc


        # ignore sites that have a different response from the link
        if(source_url_netloc not in self.urls.keys()):
            print(source_url_netloc)
            print("buggy url")
            return



        self.logger.info("Currently on page: %s", response.url)


        depth = self.urls[source_url_netloc]['depth']

        out_links = []

        for a in response.xpath('//a/@href'):
            
            # get the url, parse the url to get the netloc
            # we store the url in our dictionary to avoid different schemes 
            # being assigned to different keys

            url = a.get()
            parser = urlparse(url)
            url_netloc = parser.netloc

            if(url_netloc != ''):
                # has a netloc

                # check if the url is "external" (includes local subdomains, e.g. maps.google.com)
                if(url_netloc != source_url_netloc):
                    # full_url = parser.scheme + "://" + parser.netloc
                    out_links.append(url_netloc)

                # else doesnt have a netloc
        
        
        for link in out_links:

            if link not in self.urls.keys():
                # add the outbound link to the "graph"
                if link not in self.urls[source_url_netloc]:
                    self.urls[source_url_netloc]['data'].append(link)
                
                # add the url to self.urls as a key
                if link not in self.urls.keys():
                    self.urls[link] = None

                # crawl the outbound link
                self.urls[link] = dict()
                self.initialize_data(link, depth + 1)

                if(depth < self.MAX_DEPTH):

                    yield scrapy.Request(
                        url=self.unparse(link), 
                        headers={'User-Agent': 'Mozilla/5.0'},
                        callback=self.parse,
                        errback=self.error_handler
                    )

                else:
                    print("-------------crawl finished-------------")
                    self.crawl_finished()

    def unparse(self, link):
        unparsed_link = "https://"
        if 'www.' not in link:
            unparsed_link += "www."


        unparsed_link += link
        return unparsed_link
        

    def crawl_finished(self):
        # crawl is finished

        [print() for i in range(5)]
        print("urls dict ------------------------") 
        print(self.urls)
        [print() for i in range(5)]

    def get_cache(self):
        return self._cache

        # parser = urlparse(url)
        # parser.netloc is same?

    def initialize_data(self, dict_loc, depth):
        # initialize the data representation for each website/node
        # mainly doing this for depth (crawl to x depth)
        # for now, 'data' is just a list of the outbound links from a website
        self.urls[dict_loc]['data'] = []
        self.urls[dict_loc]['depth'] = depth

        return

if __name__ == "__main__":
    test_cache = dict()
    test_cache['amazon.com'] = []
    process = CrawlerProcess( {
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    })
    process.crawl(SurfSpider, dict())
    process.start()
        
