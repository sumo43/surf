import scrapy
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy import signals

from store_data import StoreData

class SurfSpider(CrawlSpider):

    name = "surf_spider"

    # TODO make this better
    # crawl outbound links up to this depth, to form a graph (hopefully)
    # depth 0-2 is already a lot of links, so that's all we're doing for now
    # now using depth middleware
   

    # TODO figure out how to crawl external links only, maybe through rules?
    # TODO figure out how to use rule to only crawl external links


    # TODO figure out how to crawl amazon + other sites with robots.txt
    # can use a proxy, or make it look like a real user somehow?
    # rate limit?

    # TODO look into ip ban

    rules = (
        Rule(LinkExtractor(allow=('amazon',))),
        Rule(LinkExtractor(allow=('prime',)))
    )

    

    
    # a dict representing the connections between the urls
    urls = dict()

    # root (starting) url
    root_url = None

    def __init__(self, root_url):
        self.root_url = root_url


    def error_handler(self, err):
        print("an error happened")


    def start_requests(self):


        self.urls[root_url] = dict()
        self.initialize_data(root_url, 0)

        yield scrapy.Request(
            url=self.unparse(root_url),
            headers = {'User-Agent': 'Mozilla/5.0'},
            callback=self.parse,
            errback=self.error_handler
        )
    

    # use callback with spider_closed signal
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(CrawlSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        spider.logger.info("spider closed %s", spider.name)
        self.crawl_finished()
       
    

    def crawl_url(self, url):
        if(self.urls[url]['depth'] < MAX_DEPTH):
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


                yield scrapy.Request(
                    url=self.unparse(link), 
                    headers={'User-Agent': 'Mozilla/5.0'},
                    callback=self.parse,
                    errback=self.error_handler
                )


    def unparse(self, link):
        unparsed_link = "https://"
        if 'www.' not in link:
            unparsed_link += "www."


        unparsed_link += link
        return unparsed_link
        

    def crawl_finished(self):
        # crawl is finished

        StoreData(self.urls)
          
        

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

def runSpider():
    test_cache = dict()
    test_cache['amazon.com'] = []
    process = CrawlerProcess( {
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    })
    process.crawl(SurfSpider, dict())
    process.start()



if __name__ == "__main__":
          
